# Daddo um número inteiro não negativo meu_numero
# retorne a raiz quadrada do meu_numero arredondado para o número inteiro mais próximo
# O número inteiro retornado também deve ser positivo.

# 1. O que é uma raiz quadrada
# 2x2=4 -> raiz de 4 é 2

# 2. O que é uma biblioteca
import math

# 3. Escrevendo a solução para o problema.

meu_numero = 144
resultado = math.sqrt(meu_numero)
print(resultado)

print("-------------------------------------------")

# Dada uma string minha_string, retorne o número de segmentos da string.
# Um segmento é definido como uma sequência contínua de caracteres não espaciais.

minha_string = "Opa, meu nome é Zé"
meu_array = minha_string.split()
print(meu_array)
print(len(meu_array))

print("-------------------------------------------")

# Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguinte caso é válido:
# Todas as letras desta palavra são maiúsculas, como "EUA".
# Dada uma palavra de string, retorne verdadeiro se o uso de letras maiúsculas está correto.

minha_string = "GATTO"

contador = 0

for letra in minha_string:
    if letra.isupper():
        contador += 1

print(contador)
print(len(minha_string))

if contador == len(minha_string):
    print("APROVADO")
else:
    print("REPROVADO")

print("-------------------------------------------")

# Dada uma string minha_string que consiste em palavras e espaços, retorne o comprimento da última palavra da string.

minha_string = "     fly   to   the  moon  "
meu_array = minha_string.split()

print(len(meu_array[-1]))

print("-------------------------------------------")

# Dado um array meu_array de tamanho n, retorne o elemento majoritario.
# O elemento majoritário é aquele que aparece mais [n/2] vezes.
# Você pode assumir que o elemento majoritário sempre existe no array.

meu_array = [3,2,3]
n = len(meu_array)
item_majo = n/2

meu_dicionario = {}

for item in meu_array:
    if item not in meu_dicionario:
        meu_dicionario[item] = 1
    else:
        meu_dicionario[item] += 1

for chave, valor in meu_dicionario.items():
    if valor >= item_majo:
        print(chave)

print("-------------------------------------------")

# Retorne a média de todos os salarios, com exceção do maior e menor

array_salario = [3000,4000,5000,1000,2000]
novo_array = sorted(array_salario)
novo_array.remove(novo_array[0])
novo_array.remove(novo_array[-1])
print(novo_array)

media = 0
for salario in novo_array:
    media += salario

print(media)
print(media//len(novo_array)) # Divisão de números inteiros

print("-------------------------------------------")

# Dado um array inteiro meu_array, retorne verdadeiro se algum valor aparecer pelo menos duas vezes no array
# E retorne falso se cada elemento for distinto.

meu_array = [1,1,2,3,6,6,5,5,6,4,4,8,9,7]
meu_dicionario = {}

for numero in meu_array:
    if numero not in meu_dicionario:
        meu_dicionario[numero] = 1
    else:
        meu_dicionario[numero] += 1

for chave, valor in meu_dicionario.items():
    if valor >= 2:
        print(f"{chave}: {valor} - True")
    else:
        print(f"{chave}: {valor} - False")

print("-------------------------------------------")

# Dado um array meu_array. Definimos uma soma acumulada de um array como runningSum[i] = sum(meu_array[0] + meu_array[i]).
# Retorne a soma acumulada de meu_array.
# Exemplo: 1, 1+2, 1+2+3, 1+2+3+4.

meu_array = [4,3,2,1]
resultado_array=[]

soma = 0
for numero in meu_array:
    print(f"{soma}+{numero}")
    soma += numero
    print(f"= {soma}")

"""for numero in meu_array:
    soma += numero
    resultado_array.append(soma)

print(resultado_array)"""
