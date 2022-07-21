import os
from geracao_janela import *
import tweepy
from dotenv import load_dotenv
import PySimpleGUI as sg
import analise_tweets

def main():
    # Autorizações --> Dessa forma deixamos escondidas as chaves de autenticação.
    load_dotenv()

    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    window = gerarJanela("Digite o tópico a ser analisado:")
    # Entrada de dados do usuário
    botao, query = window.read()

    if window.was_closed() or botao == "-EXIT-" or query['-TOPIC-'] == "":
        return None

    window.close()
    window = gerarJanela("Digite quantos tweets deseja analisar:")
    botao, qtd = window.read()

    if window.was_closed() or botao == "-EXIT-" or qtd['-TOPIC-'] == "":
        return None

    qtd_resultados = int(qtd["-TOPIC-"])

    # Definindo limites máximos e mínimos:
    if qtd_resultados < 10:
        qtd_resultados = 10

    elif qtd_resultados > 75:
        qtd_resultados = 75
    window.close()
    analise_tweets.analisa_tweets(api, query["-TOPIC-"], qtd_resultados)

main()