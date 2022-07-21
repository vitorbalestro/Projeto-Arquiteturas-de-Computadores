def encontrar_chave() -> str:
    """
    Função que busca a chave da OpenAI em um arquivo pré-definido.
    Caso encontre, a chave será retornada (String). Caso contrário, 
    a string 'Error' é retornada.
    """

    try:
        with open("chave_openai.bin", "rb") as arquivo:
            chave = arquivo.read()
            chave_encontrada = chave.decode("ascii")  # Decodifica a string encontrada.

            return chave_encontrada
    
    except FileNotFoundError:
        return "Error"


def alterar_chave(chave_nova):
    """
    Função que insere uma chave (String) em um arquivo binário pré-definido.
    """

    # Sobrescreve o que estiver escrito (Se existir algo escrito anteriormente).
    with open("chave_openai.bin", "wb") as arquivo:
        chave_encode = chave_nova.encode("ascii")

        arquivo.write(chave_encode)
