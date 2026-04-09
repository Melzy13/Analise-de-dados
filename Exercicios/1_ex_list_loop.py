# Exercício sobre Listas

# 1.	Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".
frutas = ["maçã", "banana", "laranja", "uva"]


# 2.	Imprima o primeiro e o último elemento da lista.
primeiro_elemento = frutas[0]
ultimo_elemento = frutas[-1]

print("Primeiro elemento:",primeiro_elemento)
print("Último elemento:",ultimo_elemento)


# 3.	Adicione a fruta "manga" ao final da lista.
frutas.append("manga")
print("Frutas:",frutas)


# 4.	Remova a fruta "banana" da lista.
frutas.remove("banana")
print("Frutas:",frutas)


# 5.	Substitua "laranja" por "abacaxi".
frutas[1] = "abacaxi"
print("Frutas:",frutas)


# 6.	Crie uma lista numeros contendo os números de 1 a 10.
numeros = list(range(1, 11))
print("Números:",numeros)


# 7.	Calcule e imprima a soma de todos os números da lista.
soma = sum(numeros)
print("Soma:",soma)


# 8.	Encontre e imprima o maior e o menor número da lista.
maior_numero = max(numeros)
menor_numero = min(numeros)

print("Maior número:", maior_numero)
print("Menor número:", menor_numero)


# 9.	Inverta a ordem dos elementos na lista e imprima a lista invertida.
inverso = numeros.reverse()
print("Inverso:", numeros)


# 10.	Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]


# 11.	Ordene a lista cidades em ordem alfabética.
cidades.sort()
print("Cidades:",cidades)


# 12.	Adicione a cidade "Port"o Alegre" ao final da lista.
cidades.append("Porto Alegre")
print("Cidades:",cidades)


# 13.	Encontre o índice da cidade "Curitiba" na lista.
cidades.index("Curitiba")


# 14.	Remova a cidade "Rio de Janeiro" da lista.
cidades.remove("Rio de Janeiro")
print("Cidades:",cidades)



# 15.	Crie duas listas lista1 e lista2, onde lista1 contém os números [1, 2, 3] e lista2 contém os números [4, 5, 6].
lista1 = list(range(1, 4))
lista2 = list(range(4, 7))

print("Lista 1:",lista1)
print("Lista 2:",lista2)


# 16.	Concatene lista1 e lista2 em uma nova lista lista3.
lista3 = lista1 + lista2


# 17.	Imprima lista3.
print("Lista 3:",lista3)


# 18.	Crie duas listas animais_domesticos e animais_selvagens, onde animais_domesticos contém ["cachorro", "gato", "coelho"] e animais_selvagens contém ["leão", "tigre", "urso"].
animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]


# 19.	Concatene as duas listas em uma nova lista todos_animais.
todos_animais = animais_domesticos + animais_selvagens


# 20.	Imprima todos_animais.
print("Todos os animais:",todos_animais)


# Looping com for

# 21.	Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".
nomes = ["Ana", "Pedro", "Maria", "João"]


# 22.	Utilize um loop for para imprimir cada nome da lista.
for nome in nomes:
    print(nome) #para cada nome em nomes(lista), print o nome.


# 23.	Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.
nomes_maiusculos = []

for nome in nomes:
    nomes_maiusculos.append(nome.upper())

print(nomes_maiusculos)


# 24.	Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares.
numeros = list(range(1, 21))

for numero in numeros:
    if numero % 2 == 0: # se o número for dividido (%) por 2 e não deixar resto (ou seja ser X,0), print o número.
        print(numero)


# 25.	Usando a lista numeros, utilize um loop for para criar uma nova lista quadrados contendo o quadrado de cada número.
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2) # ** 2 = elevado ao quadrado
print(quadrados)


# 26.	Crie uma lista palavras contendo: "python", "java", "c", "javascript". Utilize um loop for para imprimir o tamanho (número de letras) de cada palavra.
palavras = ["python", "java", "c", "javascript"]
numero_letras = []

for palavra in palavras:
    numero_letras.append(len(palavra)) # Para cada palavra em palavras (lista), em numero_letras adicione o número referente contagem de letras dessa palavra.

print(numero_letras)


# 27.	Crie uma lista idades contendo [12, 18, 25, 40, 60]. Utilize um loop for para imprimir "maior de idade" se a idade for >= 18 ou "menor de idade" se for < 18.
idades = [12, 18, 25, 40, 60]

for idade in idades:
    if idade >= 18:
        print("maior de idade")
    else:
        print("menor de idade")


# 28.	Crie uma lista notas contendo [5.5, 7.0, 8.3, 4.9, 6.2]. Utilize um loop for para contar quantos alunos estão aprovados (nota >= 7) e quantos estão reprovados (nota < 7).
notas = [5.5, 7.0, 8.3, 4.9, 6.2]

aprovados = 0
reprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1

print("Alunos aprovados:", aprovados)
print("Alunos reprovados:", reprovados)


# 29.	Crie uma lista compras com ["arroz", "feijão", "batata", "carne"]. Utilize um loop for para imprimir cada item precedido da frase "Preciso comprar: ".
compras = ["arroz", "feijão", "batata", "carne"]

for item in compras:
    print("Preciso comprar:", item)


# Looping usando while

# 30. Escreva um programa que use um loop while para imprimir os números de 1 a 10.
num = 1

while num <= 10:
    print(num)
    num += 1 # Enquanto num (número 1) for menor ou igual a 10, print num, mas some num a 1.


# 31. Usando um loop while, peça para o usuário digitar um número inteiro. O programa deve parar quando o usuário digitar o número 0.
num = int(input("Digite um número inteiro:"))

while num != 0: #enquanto num for diferente (!=) de 0...
    print("Você digitou:", num)
    num = int(input("Digite um número inteiro:"))

print("Você digitou: 0")
print("Programa encerrado.")


# 32. Utilize um loop while para calcular a soma dos números de 1 a 100.
soma = 0
num = 1

while num <= 100:
    soma += num
    num += 1

print("A soma dos números de 1 a 100 é:", soma)


# 33. Peça para o usuário adivinhar um número secreto (por exemplo, 7). Use um loop while para continuar pedindo até que ele acerte.
secreto = 7
palpite = int(input("Adivinhe o número secreto: "))

while palpite != secreto:
    print("Errado, tente novamente!")
    palpite = int(input("Adivinhe o número secreto: "))

print("Parabéns, você acertou!")


# 34. Crie um loop while que imprima todos os números pares de 2 até 20.
num = 2
while num <= 20:
    print(num)
    num += 2