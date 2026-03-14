# Exercício 1: Criando um Dicionário
# Crie um dicionário chamado 'aluno' com as seguintes chaves:
# - 'nome': contendo um nome fictício,
# - 'idade': contendo a idade do aluno,
# - 'curso': contendo o curso que ele está matriculado.
# Após criar o dicionário, exiba seus valores no seguinte formato:
# Nome: <nome>
# Idade: <idade>
# Curso: <curso>
aluno = {
    "nome": "Melissa",
    "idade": 18,
    "curso": "Administração"
}

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])


# Exercício 2: Manipulação de Dicionário
# Dado o dicionário abaixo:
# produto = {
#     "nome": "Teclado Mecânico",
#     "preco": 350.00,
#     "estoque": 10
# }
produto = {
     "nome": "Teclado Mecânico",
     "preco": 350.00,
     "estoque": 10
 }

# 1. Adicione uma nova chave chamada 'marca' com um valor de sua escolha.
produto["marca"] = "Melissa"

# 2. Atualize o preço do produto para R$ 320,00.
produto["preco"] = 320.00

# 3. Reduza o estoque em 2 unidades.
produto["estoque"] = 8
# ou
produto["estoque"] -= 2

# 4. Remova a chave 'marca' do dicionário.
del produto["marca"]

# 5. Exiba o dicionário atualizado.
print(produto)


# Exercício 3: Iterando sobre um Dicionário
# Dado o dicionário:
# notas = {
#     "Alice": 8.5,
#     "Bruno": 7.0,
#     "Carla": 9.2,
#     "Daniel": 6.8
# }
notas = {
     "Alice": 8.5,
     "Bruno": 7.0,
     "Carla": 9.2,
     "Júlia": 6.8
 }

# 1. Itere sobre o dicionário e exiba os nomes dos alunos e suas respectivas notas.
for nome, nota in notas.items(): # O .items() serve para pegar ao mesmo tempo a chave e o valor de cada entrada do dicionário.
    print("Aluno:", nome, "| Nota:", nota)
          
# 2. Calcule a média das notas e exiba o resultado.
media = sum(notas.values()) / len(notas)
print("Média das notas:", media)


# Exercício 4: Soma de Valores
# Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
# Exemplo:
# numeros = {"a": 10, "b": 20, "c": 30}
# Saída esperada: 60
numeros = {"a": 10, "b": 20, "c": 30}

soma = 0
for valor in numeros.values():
    soma += valor

print("Soma dos valores:", soma)


# Exercício 5: Contagem de Itens Repetidos
# Dado uma lista de elementos, conte a frequência de cada elemento utilizando um dicionário.
# Exemplo:
# lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
# Saída esperada: {'maçã': 3, 'banana': 2, 'laranja': 1}
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]

frequencia = {}

for item in lista:
    if item in frequencia:
        frequencia[item] += 1
    else:
        frequencia[item] = 1 # “Para cada item da lista, se ele já está no dicionário, aumente sua contagem em 1; se não está, crie a chave com valor 1.

print(frequencia)

# Exercício 6: Filtrando Dicionário
# Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
# Exemplo:
# produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# Saída esperada: {"mochila": 80, "notebook": 3000}
produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}

filtrados = {}
for nome, preco in produtos.items():
    if preco > 50:
        filtrados[nome] = preco

print(filtrados)

# Exercício 7: Tradutor Simples
# Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
# Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
# Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".
tradutor = {
    "apple": "maçã",
    "banana": "banana",
    "book": "livro",
    "car": "carro"
}

palavra = input("Digite uma palavra em inglês: ")

if palavra in tradutor:
    print("Tradução:", tradutor[palavra])
else:
    print("Palavra não encontrada")


# Exercício 8: Lista de Compras
# Crie um dicionário onde as chaves são nomes de produtos e os valores são quantidades.
# Permita ao usuário adicionar produtos, atualizar quantidades e remover itens.
# No final, exiba a lista completa de compras.
compras = {}

while True:
    print("\n1 - Adicionar produto")
    print("2 - Atualizar quantidade")
    print("3 - Remover produto")
    print("4 - Exibir lista")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        compras[produto] = quantidade

    elif opcao == "2":
        produto = input("Nome do produto: ")
        if produto in compras:
            quantidade = int(input("Nova quantidade: "))
            compras[produto] = quantidade
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        produto = input("Nome do produto: ")
        if produto in compras:
            del compras[produto]
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        print("Lista de compras:", compras)

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")


    # OUTRA OPÇÃO
# Criando o dicionário de compras
compras = {
    "arroz": 2,
    "feijão": 1,
    "leite": 3
}

# Adicionar um novo produto
compras["pão"] = 5

# Atualizar a quantidade de um produto existente
compras["leite"] = 4

# Remover um produto
del compras["feijão"]

# Exibir lista final
print("Lista de compras:", compras)

# Exercício 9: Dicionário Aninhado
# Crie um dicionário chamado 'turma' onde as chaves são nomes de alunos e os valores são dicionários contendo:
# - "idade" (inteiro),
# - "notas" (lista de três notas).
# Exemplo de estrutura:
# turma = {
#     "Ana": {"idade": 17, "notas": [8, 9, 7]},
#     "Pedro": {"idade": 18, "notas": [6, 7, 8]},
#     "Mariana": {"idade": 17, "notas": [9, 10, 8]}
# }
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}

# 1. Adicione um novo aluno ao dicionário.
turma["Lucas"] = {"idade": 18, "notas": [7, 8, 9]}


# 2. Calcule a média de notas de cada aluno e exiba no formato:
#    Ana: Média 8.0
#    Pedro: Média 7.0
#    Mariana: Média 9.0
for nome, dados in turma.items(): # Para cada nome e dado de turma...
    media = sum(dados["notas"]) / len(dados["notas"]) # faça uma média. Média é (a soma dos dados(notas)) dividido pela (contagem do número de dados(notas)).
    print(f"{nome}: Média {media:.1f}") #:.f = Mostra o número com uma casa decimal.
                                        # O f permite usar uma variavel que ele substituirá pelo valor.

# 3. Encontre o aluno com a maior média e exiba o nome dele.


# Exercício 10: Cadastro de Funcionários
# Crie um programa que permita cadastrar funcionários em uma empresa.
# O programa deve permitir adicionar funcionários com os seguintes dados:
# - Nome
# - Cargo
# - Salário
# Os funcionários devem ser armazenados em um dicionário onde a chave é o nome e o valor é outro dicionário com os dados do funcionário.
# O programa deve permitir consultar funcionários pelo nome e exibir suas informações.

