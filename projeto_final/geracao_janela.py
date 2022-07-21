"""Funções para criação das janelas."""

import PySimpleGUI as sg


def main_menu():
    """
    Função que retorna a janela do Menu Principal.
    """

    layout = [
        [sg.Text("Verificador de Campanhas do Twitter", pad=(20, 20), font=("Arial", 15))],
        [sg.Button("Iniciar checagem - TrendTopic mais comentada", pad=(40, 5), key="-CHECK1-")],
        [sg.Button("Iniciar checagem - Tópico personalizado", pad=(60, 5), key="-CHECK2-")],
        [sg.Button("Inserir ou alterar chave da OpenAI", pad=(80, 5), key="-CHNGKEY-")],
        [sg.Cancel(button_text="Sair", key="-EXIT-", pad=(170, 40))]
    ]

    window = sg.Window("Verificador de Campanhas", layout, size=(400, 300))

    return window


def gerarJanela(text):
    """
    Função que retorna uma janela de inserção genérica (Apenas o texto é alterado.).
    """

    layout = [
            [sg.Text(text)],
            [sg.Input(key="-TOPIC-")],[sg.Submit(button_text="Ok", key="-PROCEED-"),
            sg.Cancel(button_text="Cancelar", key="-CANCELAR-")]]
              # Layout a ser utilizado na janela.

    window = sg.Window("Verificador de Campanhas", layout)  # Definindo a janela

    return window

