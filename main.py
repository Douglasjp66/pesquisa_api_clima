import requests
from config import URL_BASE, CHAVE_API

nome_cidade = input('Insira o nome da cidade: ')

#id={city id}&appid={API key}
#URL concatenada
url_completa = f"{URL_BASE}q={nome_cidade}&appid={CHAVE_API}"
#print(url_completa)

dados_recebidos = requests.get(url_completa).json()
print(dados_recebidos)

if dados_recebidos ['cod'] != '404':
    principal = dados_recebidos['main']
    #print(principal)

    #dados da chave main
    temperatura_corrrente = principal['temp']
    pressao_corrente = principal['pressure']
    humidade_corrente = principal['humidity']

    #dados da chave weather
    clima = dados_recebidos['weather']
    print(clima)
    descricao_clima = clima[0]['description']
    #print(descricao_clima)
    print(f"\nTemperatura = {round(temperatura_corrrente - 273.15,1)}°C.")
    print(f"Pressão atmosférica = {pressao_corrente} hPa.")
    print(f"Humidade corrente = {humidade_corrente} %.")
    print(f"Descrição = {descricao_clima}.")
else:
    print("Cidade não encontrada. Tente novamnete !")


