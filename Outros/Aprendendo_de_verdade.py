
import pandas

data = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

dataframe = pandas.DataFrame(data)

print(dataframe) 

import pandas as pd # Com isso posso colocar só "pd" nas formulas ao inves de "pandas".
                      # Exemplo: dataframe = pandas.DataFrame(data)  =  dataframe = pd.DataFrame(data)



import pandas as pd

lista = [1, 7, 2]

emcoluna = pd.Series(lista) # Transforma uma lista simples em uma Series do Panda, ou seja, transforma a lista em uma coluna com índice.

print(emcoluna) 



# Para dar nome aos índices.
import pandas as pd

lista = [1, 7, 2]

emcoluna = pd.Series(lista, index = ["x", "y", "z"])

print(emcoluna)



# Ou crie índices com dicionário
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390} # Dicionário

emcoluna = pd.Series(calories)

print(emcoluna)



# DataFrame
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

dataframe = pd.DataFrame(data)

print(dataframe)
print(dataframe.loc[0])

dataframe = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(dataframe)

print(dataframe.loc["day2"])



import pandas as pd

df = pd.read_csv('data.csv') # Comando: Pandas pegue o arquivo 'data.csv' e leia. Ele se chamará df.

print(df) 
print(df.to_string())  # Para imprimir o todo DataFrame. Se você tiver um DataFrame grande, o Pandas retornará apenas as 5 primeiras linhas e as 5 últimas linhas


