from datetime import datetime
import pytz
import json
from geracao_janela import *
import tweepy

import tt_ia
import tt_openai
import geracao_pdf

BRASIL_ID = "23424768"  # Código de localização do Brasil -> Usamos para encontrar trendtopics no Brasil.


def encontrar_trending_topic(api) -> str:
    """
    Função que, dada a api do Twitter, retorna a trendtopic mais comentada no momento no Brasil.
    """

    brasil_trends = api.get_place_trends(BRASIL_ID)  # Encontra as trendtopics no momento no Brasil e retorna um Json.
    trends = json.loads(json.dumps(brasil_trends, indent=1))  # Arruma o Json
    trendtopic = trends[0]["trends"][0]["name"].strip("#")  # Encontra a trendtopic mais comentada.

    return trendtopic  # Retorna a trendtopic mais comentada no momento. (String)


def analisa_tweets(api, query, qtd_tweets, chave_openai, nome_pdf):
    """
    Função que, passados a api, o query (Tópico a ser analisado), a quantidade de tweets solicitada, 
    a chave da OpenAI e o nome do pdf que será gerado, analisa os 'qtd_tweets' últimos tweets sobre o tópico
    escolhido.
    
    A função utiliza duas IAs para verificar se um certo usuário possui comportamentos de um bot.
    Ao final da análise, é dada uma chance, em porcentagem, de que o tópico em questão esteja sendo 
    impulsionado artificialmente. Além disso, um pdf com as informações obtidas é gerado.
    """

    # Carregando a IA feita pelo Gabriel.
    clf = tt_ia.load_AI('new_SVC_tweet.pkl')

    # Somatório das porcentagens de chances de usuários terem atitude suspeita
    somatorio = 0

    # Vár. para guardar a quantidade de usuários com atitude suspeita encontrada durante análise
    usuarios_suspeitos = 0

    # Captura do momento da análise. (Data + Hora) --> Baseado na TimeZone de São Paulo.
    momento_analise = datetime.now(pytz.timezone("America/Sao_Paulo"))
    horario_analise = momento_analise.strftime("%H:%M:%S")
    dia_analise = momento_analise.strftime("%d/%m/%Y")
    
    # Procurando os N tweet recentes, excluindo retweets
    for tweet in tweepy.Cursor(api.search_tweets, q=f"{query} exclude:retweets", result_type="recent", tweet_mode="extended").items(qtd_tweets):
        user = api.get_user(user_id=tweet.author.id)
        data = tt_ia.transform_into_data(user)  # Transforma o usuário em um DataSet válido para a IA.
        pred = tt_ia.get_prediction(clf, data)  # IA faz as análises.

        if pred[0][0] == "bot":  # Caso a IA identifique um usuário com atividade suspeita, soma sua porcentagem de chance e aumenta a quantidade de usuários suspeitos encontrados.
            somatorio += pred[1][0][0]  # Soma a porcentagem do usuário ter atitude suspeita
        
        else:  # Caso a IA não identifique o usuário como suspeito, pegamos o tweet do usuário e o analisamos.
            resposta = tt_openai.human_or_bot(tweet.full_text, chave_openai)  # Utilização da OpenAI.

            if "robot" in resposta or "Robot" in resposta:  # Se OpenIA definir como suspeito, usuarios_suspeitos += 1 e somatório de porcentagens também aumenta.
                somatorio += pred[1][0][0]  # Aumento a porcentagem com base no que foi definido pela nossa IA.

    porcentagem_final = (somatorio / qtd_tweets) * 100  # Cálculo da média das porcentagens.
    qtd_media_user_suspeito = round(somatorio, 2)  # Arrendonda a quantidade média de usuários suspeitos encontrados.
    geracao_pdf.gerar_pdf(f"{nome_pdf}", query, qtd_tweets, horario_analise, dia_analise, qtd_media_user_suspeito, porcentagem_final)  # Gera o PDF.
