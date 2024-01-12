import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

#cotacao_dolar = cotacoes['USDBRL']["bid"]

precos = {}

for i in cotacoes:
    precos[i] = cotacoes[i]["bid"]
    # nome = cotacoes[i]["name"]
    # valor = cotacoes[i]["bid"]
    # print(valor)
    # print(nome)
    # print(precos)

for i in precos:
    print(f"{i}: {precos[i]}")


for i in cotacoes:
    nome = cotacoes[i]["name"]
    valor = cotacoes[i]["bid"]
    print(f"{nome}: {valor}")