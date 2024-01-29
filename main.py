import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

#cotacao_dolar = cotacoes['USDBRL']["bid"]
print(cotacoes)

precos = {}

for i in cotacoes:
    precos[i] = cotacoes[i]["bid"]


for i in precos:
    print(f"{i}: {precos[i]}")


# outro modo de fazer
for i in cotacoes:
    nome = cotacoes[i]["name"]
    valor = cotacoes[i]["bid"]
    print(f"{nome}: {valor}")