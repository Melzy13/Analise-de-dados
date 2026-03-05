"""
Aula - Exercicios de Listas em Python
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e compare com o resultado esperado (quando informado).

Regra da aula:
- Nao use IA para gerar resposta final.
- Resolva passo a passo e valide com print.
"""

# ------------------------------
# BLOCO 1: fundamentos
# ------------------------------

vendas_semana = [1200, 980, 1430, 1100, 1600]

# Exercicio 1:
# Mostre:
# a) numero de dias vendidos
num_dias = len(vendas_semana) #len: Retorna o numero de elementos existentes na lista.

# b) total vendido na semana
total_vendas = sum(vendas_semana)

# c) maior e menor venda diaria
maior_venda = max(vendas_semana)
menor_venda = min(vendas_semana)

# RESOLUCAO: complete aqui

print("Número de dias vendidos:", num_dias)
print("Total vendido na semana:", total_vendas)
print("Maior venda diária:", maior_venda)
print("Menor venda diária:", menor_venda)


# Exercicio 2:
# Acesse e mostre:
# a) primeira venda
primeira_venda = vendas_semana[0]

# b) ultima venda
ultima_venda = vendas_semana[-1]

# c) vendas do meio (sem primeira e ultima)
vendas_meio = vendas_semana[1:-1] #Retorna o segundo termo (1) até o anterior ao último (-1).

# RESOLUCAO: complete aqui
print("Primeira venda:", primeira_venda)
print("Última venda:", ultima_venda)
print("Vendas do meio:", vendas_meio)

# -----------------------------------
# BLOCO 2: alterar e limpar
# -----------------------------------

custos_marketing = [350, 420, 390, 410]

# Exercicio 3:
# a) Adicione um novo custo de 460 no final
custos_marketing.append(460)
# usando insert para colocar no final
custos_marketing.insert(len(custos_marketing), 460) #len(custos_marketing) é o número de elementos existentes na lista, ou seja retoma a posição do último elemento.

# b) Insira 300 no inicio da lista
custos_marketing.insert(0, 300)

# c) Remova o valor 390
custos_marketing.remove(390)

# RESOLUCAO: complete aqui
print("Lista final de custos:", custos_marketing)


# Exercicio 4:
# A lista abaixo tem um lancamento duplicado por erro.
# Remova somente uma ocorrencia de 1200.

vendas_com_erro = [900, 1200, 1500, 1200, 1800]

# RESOLUCAO: complete aqui
vendas_com_erro.remove(1200)
print("Lista corrigida:", vendas_com_erro)

# -----------------------------------------
# BLOCO 3: ordenacao e filtragem
# -----------------------------------------

ticket_medio_filiais = [85, 120, 73, 150, 99, 135]

# Exercicio 5:
# a) Crie uma nova lista em ordem crescente (sem perder a original)
# b) Crie outra em ordem decrescente
# c) Mostre as tres listas

# RESOLUCAO: complete aqui


# Exercicio 6:
# Gere uma lista apenas com tickets acima de 100.
# Dica: use for + if, ou list comprehension.

# RESOLUCAO: complete aqui


# ---------------------------------------
# BLOCO 4: agregacao e tomada
# ---------------------------------------

faturamento_diario = [2100, 1800, 2500, 1950, 2300]

# Exercicio 7:
# a) Calcule a media de faturamento diario
# b) Conte quantos dias ficaram acima da media
# c) Mostre os valores desses dias

# RESOLUCAO: complete aqui


# ---------------------------------------
# BLOCO 5: desafio final guiado
# ---------------------------------------

# Cenário:
# Sua empresa registrou vendas por vendedor na semana.
vendas_vendedor = [450, 520, 610, 480, 700, 530, 620]

# Exercicio 8 (desafio):
# 1) Calcule total e media semanal
# 2) Crie uma lista com vendas acima de 550
# 3) Mostre os 3 maiores valores de venda
# 4) Informe quantos dias ficaram abaixo de 500

# RESOLUCAO: complete aqui


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Sei criar listas e acessar por indice
# [ ] Sei usar len, sum, min, max
# [ ] Sei adicionar/remover itens
# [ ] Sei ordenar sem perder dados originais
# [ ] Sei filtrar listas com condicoes
# [ ] Sei aplicar listas em cenarios de negocio

