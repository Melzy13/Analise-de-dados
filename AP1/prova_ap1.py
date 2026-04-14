# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento

import pandas as pd

arquivo = "ncr_ride_bookings.csv"
df = pd.read_csv(arquivo)

# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
df_completed = df[df['Booking Status'] == "Completed"]

# (0,5) 2 - Qual a proporção em relação ao total de corridas?
propocao = len(df) - len(df_completed)
print(propocao)

# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
df.groupby('Vehicle Type')['Ride Distance'].mean()

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?
df["Payment Method"]

UPI = df[df['Payment Method'] == "UPI"]
len(UPI)

Debit_Card = df[df['Payment Method'] == "Debit Card"]
len("Debit Card")

Uber_Wallet = df[df['Payment Method'] == "Uber Wallet"]
len("Uber wallet")

cash = df[df['Payment Method'] == "Cash"]
len("Cash")

len(UPI) # UPI é o método de pagamento mais utilizado

# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?
sum(df['Booking Value'] == "Completed")
df["Booking Value"]

#ou

df_vcompleted = df[df['Booking Value'] == "Completed"]
len(df_vcompleted)

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?



# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;

import requests
import pandas as pd 

url = f"http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url) 
response.status_code
dados = response.json()
df = pd.DataFrame([dados])
df


# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
filtro = df["SERCODIGO"]
df.loc[filtro,:]
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.


# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE1MzgyLCJpYXQiOjE3NzQ1MjMzODIsImp0aSI6IjE4MWY0ZDBiNzFmYTQzNGFhZDY5MTI4MWFlNmJhOGVkIiwidXNlcl9pZCI6IjEwNCJ9.66MUmwS1I7INuYuqBHHKZGQMav_gjl-7CsHpXgLbbrk" 
params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
response = requests.get(
     f"{base_url}/preco/corrigido",
     headers={"Authorization": f"Bearer {token}"},
     params=params,
)



# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE1MzgyLCJpYXQiOjE3NzQ1MjMzODIsImp0aSI6IjE4MWY0ZDBiNzFmYTQzNGFhZDY5MTI4MWFlNmJhOGVkIiwidXNlcl9pZCI6IjEwNCJ9.66MUmwS1I7INuYuqBHHKZGQMav_gjl-7CsHpXgLbbrk" 
params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2026-04-01"},
 )


# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE1MzgyLCJpYXQiOjE3NzQ1MjMzODIsImp0aSI6IjE4MWY0ZDBiNzFmYTQzNGFhZDY5MTI4MWFlNmJhOGVkIiwidXNlcl9pZCI6IjEwNCJ9.66MUmwS1I7INuYuqBHHKZGQMav_gjl-7CsHpXgLbbrk" 
response = requests.get(
     f"{base_url}/bolsa/planilhao",
     headers={"Authorization": f"Bearer {token}"},
     params={"data_base": "2026-04-01"},
)

# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?
