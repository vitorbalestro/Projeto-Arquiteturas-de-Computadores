import openai


def human_or_bot(input_text, openai_key) -> str:
    """
    Função que, ao receber um texto e a chave da OpenAI, retorna se o autor
    do texto é um ser humano ou um bot. Caso seja um humano, a string 'Human' é retornada.
    Caso contrário, a string 'Robot' é retornada.
    """

    openai.api_key = openai_key  # Insere a chave da OpenAI.

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Decide whether a Tweet was made by a Human or a Robot:\n Tweet:{input_text}\nResponse:\n"
    )  # IA faz a análise.

    return response.choices[0].text


def sentiment_analysis(text, openai_key):
    openai.api_key = openai_key

    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = f"Decide whether a Tweet's sentiment is positive, negative or neutral:\n Tweet:{text}\n Response: \n"
  )
  
    return response.choices[0].text
