import os

import tweepy
import PySimpleGUI as sg
from dotenv import load_dotenv

import analise_tweets
import chave
import geracao_janela

# Pegando as chaves e senhas para a autorização
load_dotenv()  # Carrega o .env

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Fazendo a autorização da API do Twitter.
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)  # Faz as autorizações necessárias.
api = tweepy.API(auth)  # Inicializa a API

# Inicialização da janela de Menu Principal.
window_menu = geracao_janela.main_menu()  # Inicialização da janela de Menu Inicial.
analise = 0  # Variável de controle.

# Laço para rodar o menu inicial e suas subjanelas.
while True:
    # Entrada de dados do usuário
    event, value = window_menu.read()  # Leitura de eventos e valores.

    if window_menu.was_closed() or event == "-EXIT-":  # Verificação de fechamento da janela.
        break

    if event == "-CHECK1-":  # Verificando primeira opção de verificação
        chave_openai = chave.encontrar_chave()

        # Se chave não estiver salva ainda, o usuário não pode avançar na verificação.
        if chave_openai == "Error":
            sg.popup("Você precisa inserir uma chave da OpenAI para fazer uma análise!")  # Gera popup de aviso.
            continue

        # Janela de inserção da quantidade de tweets desejados.
        window_menu.hide()  # Esconde o menu principal.

        window_analise = geracao_janela.gerarJanela("Digite quantos tweets deseja analisar:")  # Inicializa nova janela.
        event, value = window_analise.read()

        if window_analise.was_closed(): # Verificação de fechamento da janela.
            break
        
        if event == "-CANCELAR-":  # Verificação de Botão 'Cancelar'.
            window_analise.close()  # Fecha janela atual.
            window_menu.un_hide()  # Mostra a janela de menu principal novamente.
            continue  # Volta para o início do laço While.

        if value['-TOPIC-'] == "":  # Verificação de inserção vazia.
            sg.popup("É preciso inserir algo válido!")  # Popup de aviso.
            window_analise.close()
            window_menu.un_hide()
            continue

        # Try/Except para checar erros na hora de usar a função 'encontrar_trending_topic"
        try:
            query = analise_tweets.encontrar_trending_topic(api)  # Busca a trend topic mais comentada no momento no Brasil.
        except:
            window_menu.close()
            window_analise.close()
            sg.popup("Algo deu errado! Verifique sua conexão e tente novamente!")
            break

        # Try/Except para checar se o valor inserido pode ser convertido para int.
        try:
            qtd_resultados = int(value["-TOPIC-"])  # qtd_resultados recebe o quer for passado na hora que o botão for apertado.
        except:
            sg.popup("Algo deu errado! Reinicie o programa e tente novamente!")
            break

        # Definindo limites máximos e mínimos para a quantidade de tweets:
        if qtd_resultados < 10:
            qtd_resultados = 10

        elif qtd_resultados > 75:
            qtd_resultados = 75
        
        window_analise.close()  # Fecha janela atual.

        # Inicialização da janela para inserir o nome do PDF a ser gerado:
        window_analise = geracao_janela.gerarJanela("Digite o nome do pdf:")  
        event, value = window_analise.read()

        if window_analise.was_closed():
            break

        if event == "-CANCELAR-":
            window_analise.close()
            window_menu.un_hide()
            continue

        if value['-TOPIC-'] == "":
            sg.popup("É preciso inserir algo válido!")
            window_analise.close()
            window_menu.un_hide()
            continue

        nome_pdf = value['-TOPIC-']

        analise = 1  # Acerta a variável de controle.
        window_menu.close()  # Fecha o menu principal.

        break

    if event == "-CHECK2-": # Verificando segunda opção de verificação
        chave_openai = chave.encontrar_chave()

        if chave_openai == "Error":
            sg.popup("Você precisa inserir uma chave da OpenAI para fazer uma análise!")
            continue

        window_menu.hide()

        # Janela de inserção de tópico a ser analisado.
        window_analise = geracao_janela.gerarJanela("Digite o tópico a ser analisado:")  
        event, value = window_analise.read()

        if window_analise.was_closed():
            break

        if event == "-CANCELAR-":
            window_analise.close()
            window_menu.un_hide()
            continue

        if value['-TOPIC-'] == "":
            sg.popup("É preciso inserir algo válido!")
            window_analise.close()
            window_menu.un_hide()
            continue

        query = value["-TOPIC-"]

        window_analise.close()

        # Janela de inserção da quantidade de tweets desejados.
        window_analise = geracao_janela.gerarJanela("Digite quantos tweets deseja analisar:")
        event, value = window_analise.read()

        if window_analise.was_closed():
            break

        if event == "-CANCELAR-":
            window_analise.close()
            window_menu.un_hide()
            continue

        if value['-TOPIC-'] == "":
            sg.popup("É preciso inserir algo válido!")
            window_analise.close()
            window_menu.un_hide()
            continue

        try:
            qtd_resultados = int(value["-TOPIC-"])
        except:
            sg.popup("Algo deu errado! Reinicie o programa e tente novamente!")
            break

        # Definindo limites máximos e mínimos:
        if qtd_resultados < 10:
            qtd_resultados = 10

        elif qtd_resultados > 75:
            qtd_resultados = 75

        window_analise.close()
        
        # Inicialização da janela para inserir o nome do PDF a ser gerado:
        window_analise = geracao_janela.gerarJanela("Digite o nome do pdf:")  
        event, value = window_analise.read()

        if window_analise.was_closed():
            break

        if event == "-CANCELAR-":
            window_analise.close()
            window_menu.un_hide()
            continue

        if value['-TOPIC-'] == "":
            sg.popup("É preciso inserir algo válido!")
            window_analise.close()
            window_menu.un_hide()
            continue

        nome_pdf = value['-TOPIC-']
        
        analise = 1
        window_menu.close()

        break

    if event == "-CHNGKEY-":  # Verificando opção de troca/inserção de chave da OpenAI
        window_menu.hide()

        # Janela de inserção/troca de chave da OpenAI
        window_chave = geracao_janela.gerarJanela("Digite a chave da OpenAI:")  
        event, value = window_chave.read()

        if event == "-CANCELAR-":
            window_chave.close()
            window_menu.un_hide()
            continue

        if value['-TOPIC-'] == "":
            sg.popup("É preciso inserir algo válido!")
            window_chave.close()
            window_menu.un_hide()
            continue

        if window_chave.was_closed():
            break
            
        chave.alterar_chave(value["-TOPIC-"])  # Utilização da função para salvar alteração da chave.
        sg.popup("Chave alterada com sucesso!")

        window_chave.close()
        window_menu.un_hide()

if analise == 1:  # Caso uma análise precise ser feita.
    window_analise.close()

    sg.popup_auto_close("A análise será iniciada em instantes! Um aviso será emitido ao término.", auto_close_duration=3)  # Popup que fecha depois de 3 segundos.

    # Try/Except para verificar possíveis erros na execução de analisa_tweets.
    try:
        analise_tweets.analisa_tweets(api, query, qtd_resultados, chave_openai, nome_pdf)
        sg.popup(f"A análise foi encerrada com sucesso! O PDF ' {nome_pdf}.pdf ' foi gerado!")  # Popup de aviso de término da análise.
    except:
        sg.popup("Algo deu errado! Verifique sua chave da OpenAI e/ou conexão e tente novamente!")
