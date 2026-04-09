import requests # Ei, Python, quero usar a biblioteca Requests dentro do meu código."
# É como um telefone que o seu programa usa para conversar com outros sites e serviços na internet.

import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2" # Endereço
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE1MzgyLCJpYXQiOjE3NzQ1MjMzODIsImp0aSI6IjE4MWY0ZDBiNzFmYTQzNGFhZDY5MTI4MWFlNmJhOGVkIiwidXNlcl9pZCI6IjEwNCJ9.66MUmwS1I7INuYuqBHHKZGQMav_gjl-7CsHpXgLbbrk" # Chave de acesso

resp = requests.get( # Para pegar informações de um endereço.
    f"{base_url}/bolsa/planilhao", # O caminho exato de onde ele deve ir buscar os dados
    headers={"Authorization": f"Bearer {token}"}, # Informações adicionais (Autorização de acesso)
    params={"data_base": "2026-03-23"},
)
dados = resp.json()
df = pd.DataFrame(dados)
maximo = df["roe"].max()
filtro = df["roe"]== maximo 
df[filtro]



import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
params = {"ticker": "MNPR3", "data_ini": "2025-03-21", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params, 
)

dados = resp.json()
df_preco = pd.DataFrame(dados)
filtro1 = df_preco["data"]=="2026-03-23"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float (preco_final)
filtro2 = df_preco["data"]== "2025-03-21"
precos_inicial = df_preco.loc[filtro2, 'fechamento'].iloc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1 


#API para pegar o Ibov
import yfinance as yf
#Get ticker data
ibov = yf.download("^BVSP", start="2001-01-01", end= "2026-03-26")
filtro1 = ibov.index == "2025-03-21"
ibov_ini = ibov[filtro1]["Close"].iloc[0]
filtro2 = ibov.index == "2026-03-23"
ibov_fim = ibov [filtro2]["Close"].iloc[0]
ibov_fim/ibov_ini - 1





import requests
import pandas as pd
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)
dados = resp.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roic", "earning_yield"]]
df2['rank_roic'] = df2 ['roic'].rank(ascending=False)
df2['rank_p_ey'] = df2['earning_yield'].rank(ascending=False)
df2["rank_final"] = (df2['rank_roic'] + df2['rank_p_ey']) / 2
df2.sort_values("rank_final", ascending=False)['ticker'][:20]  

#API para pegar os precos das acoes
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMjM0LCJpYXQiOjE3NzQzNTAyMzQsImp0aSI6IjQzNzQ0MzI3MjVlMTQ5ZGRhY2E0YWJmZWM5Njg3MjQxIiwidXNlcl9pZCI6Ijk2In0.KDIch7t2a4wHQNmiGlWY1uGG6_V5mK3XHmkdEH4eJpY"
params = {"ticker" : "BBSE3", "data_ini" : "2001-01-01", "data_fim": "2026-03-26"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params = params,
)
dados = resp.json()
df_preco = pd.DataFrame(dados)
#Preco final
filtro1 = df_preco["data"] == "2026-03-23"
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float(preco_final)