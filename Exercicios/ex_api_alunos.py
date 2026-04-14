"""
===========================================================
ATIVIDADE – CONSULTA DE DADOS VIA API
OBJETIVO:
- Consultar APIs públicas usando requests
- Entender estrutura JSON
- Transformar resposta em DataFrame
- Trabalhar com parâmetros e TOKENS
- Explorar dados externos
REGRAS:
- NÃO apagar os enunciados.
- Organizar o código.""
- Comentar cada etapa importante.
- Mostrar os resultados com print() ou DataFrame.
===========================================================
"""

# ===========================================================
# PARTE 1 – INTRODUÇÃO
# ===========================================================
"""
O que é uma API?
API (Application Programming Interface) permite que um sistema
se comunique com outro.
Quando usamos requests.get(), estamos enviando uma requisição
HTTP para um servidor que retorna dados, geralmente em JSON.
Fluxo básico:
1. Definir URL
2. Enviar requisição
3. Verificar status_code
4. Converter para JSON
5. Transformar em DataFrame (quando necessário)
"""
# ===========================================================
# PARTE 2 – VIACEP (Consulta de CEP)
# ===========================================================
"""
Site: https://viacep.com.br/
Exemplo de consulta:
https://viacep.com.br/ws/01001000/json/

Exercícios:
1. Consulte um CEP da sua escolha.
2. Verifique o status da requisição.
3. Converta a resposta para JSON.
4. Transforme em DataFrame.
5. Mostre as principais informações.
"""
# RESOLVA AQUI:
import requests # Biblioteca para fazer requisições HTTP, ou seja, para acessar APIs e obter dados.
import pandas as pd # Biblioteca para manipulação de dados, especialmente em formato de tabelas (DataFrames).

url = f"https://viacep.com.br/ws/70680250/json/" # URL do endpoint da API ViaCEP para consultar o CEP 70680250. O "f" antes da string permite usar variáveis dentro da string.
response = requests.get(url) # Envia uma requisição GET para a URL especificada e armazena a resposta na variável "response".
response.status_code # Verifica o status da requisição. Um status_code de 200 indica que a requisição foi bem-sucedida.
dados = response.json() # Converte a resposta da API, que está em formato JSON, para um dicionário Python e armazena na variável "dados".
df = pd.DataFrame([dados]) # Transforma o dicionário "dados" em um DataFrame do Pandas. O dicionário é colocado dentro de uma lista para criar uma linha no DataFrame.
df # Exibe o DataFrame resultante, mostrando as informações do CEP consultado.

# ===========================================================
# PARTE 3 – BRASILAPI
# ===========================================================
"""
Documentação:
https://brasilapi.com.br/docs # Pesquisa o link, vai em "BANKS", clica em "GET" e copia a url.
Exercícios:
1. Consulte a lista de bancos.
2. Transforme o resultado em DataFrame.
3. Conte quantos bancos existem.
4. Filtre bancos cujo nome contenha "Brasil".
Explique:
O que você percebe sobre a estrutura do JSON retornado?
"""
# RESOLVA AQUI:
url = "https://brasilapi.com.br/api/banks/v1" # URL do endpoint da API BrasilAPI para consultar a lista de bancos.
response = requests.get(url) # Envia uma requisição GET para a URL especificada e armazena a resposta na variável "response".
response.status_code # Verifica o status da requisição. Um status_code de 200 indica que a requisição foi bem-sucedida.
dados = response.json() # Converte a resposta da API, que está em formato JSON, para uma lista de dicionários Python e armazena na variável "dados".
df = pd.DataFrame(dados) # Transforma a lista de dicionários "dados" em um DataFrame do Pandas, onde cada dicionário representa uma linha.
print(df) # Exibe o DataFrame resultante, mostrando a lista de bancos.
df # Exibe o DataFrame novamente para verificar a estrutura dos dados.
print(f"Total de bancos: {len(df)}") # Imprime o total de bancos



# ===========================================================
# PARTE 4 – SERVIÇO DE DADOS IBGE
# ===========================================================
"""
Documentação:
https://servicodados.ibge.gov.br/api/docs/
Exercícios:
1. Consulte os estados brasileiros.
2. Transforme em DataFrame.
3. Mostre apenas:
   - nome
   - sigla
   - região
4. Pesquise como consultar dados de população.
Desafio:
Consultar a população total de um estado específico.
"""
# RESOLVA AQUI:
url = "https://servicodados.ibge.gov.br/api/docs/" # URL do endpoint da API do IBGE para consultar os estados brasileiros. (A URL correta para consultar os estados seria "https://servicodados.ibge.gov.br/api/v1/localidades/estados")
response = requests.get(url) # Envia uma requisição GET para a URL especificada e armazena a resposta na variável "response".
response.status_code # Verifica o status da requisição. Um status_code de 200 indica que a requisição foi bem-sucedida.
# Transforma em json e pega a chave "municipios"
dados = response.json() # Converte a resposta da API, que está em formato JSON, para uma estrutura de dados Python (geralmente uma lista ou dicionário) e armazena na variável "dados".
# Pega o primeiro elemento da lista # A resposta da API do IBGE para os estados é uma lista de dicionários, onde cada dicionário representa um estado. Pegamos o primeiro elemento da lista para acessar os dados dos municípios.
dados = dados[0] # Acessa o primeiro elemento da lista "dados", que é um dicionário representando um estado, e armazena novamente na variável "dados".
# Pega a chave "municipio" # O dicionário do estado contém uma chave "municipios" que é uma lista de dicionários, onde cada dicionário representa um município. Acessamos essa chave para obter a lista de municípios.
dados = dados["municipios"] # Acessa a chave "municipios" do dicionário "dados", que é uma lista de dicionários representando os municípios, e armazena novamente na variável "dados".
# Transforma em df # A lista de dicionários "dados" é transformada em um DataFrame do Pandas, onde cada dicionário representa uma linha.
df = pd.json_normalize(dados) # A função pd.json_normalize() é usada para "achatar" a estrutura do JSON, transformando os dados aninhados em colunas do DataFrame. Isso é útil quando o JSON tem uma estrutura hierárquica.
df # Exibe o DataFrame resultante, mostrando os dados dos municípios do estado consultado.


# ===========================================================
# PARTE 5 – IPEA DATA
# ===========================================================
"""
Documentação:
https://www.ipeadata.gov.br/api/
Exercícios:
1. Consulte os metadados de uma série.
2. Identifique:
   - nome da série
   - descrição
   - unidade
3. Consulte os valores históricos da série.
4. Transforme em DataFrame.
"""
# RESOLVA AQUI:
url = "https://www.ipeadata.gov.br/api/" # URL do endpoint da API do IPEA Data para consultar os metadados de uma série. (A URL correta para consultar os metadados de uma série seria "https://www.ipeadata.gov.br/api/odata4/Metadados('codigo_da_serie')")
response = requests.get(url) # Envia uma requisição GET para a URL especificada e armazena a resposta na variável "response".
response.status_code # Verifica o status da requisição. Um status_code de 200 indica que a requisição foi bem-sucedida.
dados =  # Converte a resposta da API, que está em formato JSON, para uma estrutura de dados Python (geralmente um dicionário) e armazena na variável "dados"
response.json() # Exibe a estrutura do JSON retornado pela API para entender como acessar os dados desejados.
# A partir da estrutura do JSON, identifique as chaves que contêm o nome da


# ===========================================================
# PARTE 6 – BANCO CENTRAL DO BRASIL (BCB)
# ===========================================================
"""
Dados Abertos BCB:
https://dadosabertos.bcb.gov.br/
Exemplo: Consulta PTAX
Parâmetros:
{
 "formato": "json",
 "dataInicial": "01/01/2024",
 "dataFinal": "31/12/2024"
}
Exercícios:
1. Consulte a cotação do dólar em 2024.
2. Transforme em DataFrame.
3. Calcule:
   - média
   - valor máximo
   - valor mínimo
4. Plote gráfico de linha.
"""
# RESOLVA AQUI:

codigo = 4189
url 

# ===========================================================
# PARTE 7 – FOOTBALL-DATA.ORG
# ===========================================================
"""
Documentação:
https://www.football-data.org/documentation/quickstart
Observação:
Essa API exige API-KEY.
Exercícios:
1. Consulte as áreas (countries).
2. Filtre o Brasil (CountryCode = "BRA").
3. Consulte competições do Brasil.
4. Consulte os times da temporada 2025.
Explique:
O que são parâmetros de consulta?
"""
# RESOLVA AQUI:



# ===========================================================
# PARTE 8 – RAPIDAPI (EXEMPLOS)
# ===========================================================
"""
Exemplos:
Tripadvisor – SearchLocation
querystring = {"query":"brasilia"}
NBA – Estatísticas de jogadores
querystring = {"game":"8133"}
Exercícios:
1. Escolha uma API do RapidAPI.
2. Faça uma consulta.
3. Transforme a resposta em DataFrame.
4. Descreva a estrutura do JSON retornado.
Desafio:
Identifique níveis aninhados no JSON.
"""
# RESOLVA AQUI:



# ===========================================================
# PARTE 9 – EXPLORAÇÃO LIVRE
# ===========================================================
"""
Pesquise APIs públicas em:
https://github.com/public-apis/public-apis
https://apilayer.com/marketplace
https://app.balldontlie.io/
Exercícios:
1. Escolha uma API pública.
2. Consulte dados.
3. Transforme em DataFrame.
4. Faça uma pequena análise exploratória.
"""
# RESOLVA AQUI:



# ===========================================================
# Revisão FINAL
# ===========================================================
"""
Responda:

1. O que é uma API?
2. O que é um endpoint?
3. O que são parâmetros?
4. O que é JSON?
5. O que é Headers?
6. O que é Token?
"""