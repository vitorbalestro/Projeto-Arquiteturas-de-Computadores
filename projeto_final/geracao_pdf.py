from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4


def mm2p(milimetros):
    """
    Função que transforma milimetros (Unidade de medida da página do Canvas) em um ponto no plano cartesiano.
    """

    return milimetros / 0.352777


def gerar_pdf(nome_pdf, topico, qtd_tweets, horario_analise, data_analise, qtd_user_suspeitos, porcentagem):
    """
    Função que gera o pdf usando os argumentos recebidos.
    """

    cnv = Canvas(f"{nome_pdf}.pdf", pagesize=A4)  # Gera o PDF e seta o tamanho da página como A4.

    cnv.setFont("Courier-Bold", 14)  # Seta fonte e tamanho.
    cnv.drawCentredString(mm2p(105), mm2p(290), "Resultados da Verificação de Impulsionamento Artificial de Campanhas")  # Escreve o título na fonte acima.

    cnv.setFont("Courier", 10)  # Muda a fonte e tamanho.
    cnv.drawCentredString(mm2p(105), mm2p(280), f"Momento da Análise: {data_analise} - {horario_analise}")
    cnv.drawString(mm2p(3), mm2p(260), f"-> Quantidade de Tweets analizados nessa amostragem: {qtd_tweets}")
    cnv.drawString(mm2p(3), mm2p(250), f"-> Tópico analisado nessa amostragem: '{topico}'")
    cnv.drawString(mm2p(3), mm2p(240), f"-> Quantidade média de usuários com atividade suspeita encontrados: {qtd_user_suspeitos}")
    cnv.drawString(mm2p(3), mm2p(230), f"-> Chance do tópico estar sendo impulsionado artificialmente durante o momento da análise: {porcentagem:.2f}%")
    cnv.drawCentredString(mm2p(105), mm2p(180), "AVISO:")
    cnv.drawCentredString(mm2p(105), mm2p(175), "Os dados aqui apresentados foram gerados por Inteligências Artificiais.")
    cnv.drawCentredString(mm2p(105), mm2p(170), "Portanto, eles são probabilísticos e imparciais.")

    cnv.save()  # Salva as alterações feitas e fecha o PDF.
