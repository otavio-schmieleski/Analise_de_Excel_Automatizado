import pandas as pd
from twilio.rest import Client
#pandas
# openpyxl
# twilio

# Your Account SID from twilio.com/console
account_sid = "AC49aeee1d24e5df81d6d2a1fcff102d5f"
# Your Auth Token from twilio.com/console
auth_token  = "e8d9ec24e0943625b9e06804bde81e45"
client = Client(account_sid, auth_token)

    # passo a passo de solucao

#abrir os 6 arquivos em excel
lista_meses = ["janeiro","fevereiro","março","abril","maio","junho"]
#para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    # vereficar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas["Vendas"] >= 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] >= 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] >= 55000, "Vendas"].values[0]
        # se for maior que 55.000 enviar mensagem por sms com nome, mes e as vendas do vendedor
        message = client.messages.create(
            to="+5546991284866",
            from_="+13612648090",
            body=f"No mes {mes} alguem bateu a meta. vendedor: {vendedor} ,com o valor de vendas de: {vendas}")
        print(message.sid)
# se nao nao faz nada




