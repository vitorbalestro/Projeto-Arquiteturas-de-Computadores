# Verificador de Campanhas do Twitter

## *Objetivos do Projeto*:
Esse projeto tem como objetivo encontrar a chance de um certo tópico/campanha no Twitter estar sendo impulsionado artificialmente, isto é, por meio do uso de bots.

## *Como utilizar*:
Para fazer uso dos códigos, é preciso primeiro fazer alguns ajustes, que serão explicados abaixo.

- Bibliotecas necessárias:
  - Tweepy ('pip install tweepy')
  - PySimpleGUI ('pip install pysimplegui')
  - ReportLab ('pip install reportlab')
  - Dotenv ('pip install python-dotenv')
  - Sklearn ('pip install sklearn')
  - Openai ('pip install openai')

- Chaves de Acesso (Tweepy): É preciso criar uma conta de desenvolvedor no Twitter para ter conseguir chaves de acesso a API. Esse tipo de conta pode
ser criada facilmente a partir [deste link](https://developer.twitter.com/en). A utilização destas chaves é explicada no próximo tópico.

- Colocar as Chaves de Acesso do Tweepy em um '.env' : Na pasta 'projeto_final', você vai encontrar o arquivo '.env_template'. Nele, está explicitado
o modelo do arquivo '.env' a ser criado. Portanto, basta criar o arquivo '.env' na pasta 'projeto_final' e colocar suas chaves seguindo o modelo
apresentado em '.env_template'.

- Chaves de Acesso (OpenAI): Para fazer as análises é preciso inserir a sua chave da OpenAI através da própria interface gráfica do programa. Ela ficará
armazenada em um arquivo .bin. Essa chave pode ser adquirida gratuitamente a partir [deste link](https://openai.com/api/). É importante lembrar que as 
chaves da OpenAI possuem um limite e, portanto, é possível que sua chave expire em algum momento. 

__Aviso__: __O arquivo '.pdf' é criado no mesmo diretório de 'main_gui.py'__.
