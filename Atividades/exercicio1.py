# Escreva um programa que receba três números e exiba o segundo maior número entre eles.
numero1 ,numero2,numero3= map(int, input().split()) 
""" split() divide essa string em pedaços usando espaços (gera uma lista de tokens), 
map(int, ) aplica int a cada token, retornando um iterador que converte os tokens em inteiros."""

# Preciso receber esses numeros
lista_numeros = [numero1, numero2, numero3]

# Criar uma lógica para ver quem é o segundo maior
lista_numeros.sort(reverse=True)

# Mostrar na tela os resultados
print(lista_numeros)
""" lista_numeros.sort() == Organiza os números em ordem crescente """