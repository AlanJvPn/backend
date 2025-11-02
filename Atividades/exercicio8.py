# Receba um número e determine se ele é uma palindromo (lê-se igual de frente para trás)

# 1. Receber um numero inteiro
numero = int(input())

# 2. Determinar se é um palíndromo
# 3. Retornar se é ou não é
string = str(numero)

if string == string[::-1]:
    print(f"{string} é um palíndromo!")
else:
    print(f"{string} não é um palíndromo!")
