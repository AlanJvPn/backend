# Receba uma lista de palavras e ordene-as em ordem alfabetica

# 1. Criar um array vazio para receber essas palavras
lista_palavras = []

# 2. Definir uma quantidade de palavras
n = int(input("Quantas palavras quer escrever? "))

# 3. Criar a logica para receber essas palavras e adicionar dentro do array
for i in range(1, n+1):
    palavra = input()
    lista_palavras.append(palavra)

# 4. Ordenar a lista
lista_palavras.sort()

# 5. Printar na tela
print(lista_palavras)