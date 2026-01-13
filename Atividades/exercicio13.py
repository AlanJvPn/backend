# Dado um array de números inteiros, retorne a soma do menor número e do maior número do array.

num_inteiros = [7,8,9,5,2,95,9,74,6,1,53,4,98,524]

# 1. Ordenar de forma crescente

num_inteiros.sort()

print(num_inteiros)

# 2. Somar os valores de ultima posição e o de primeira

valor= num_inteiros[0] + num_inteiros[-1]
print(valor)