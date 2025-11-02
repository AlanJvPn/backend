# Soma de 1 a N: Receba um número N e exiba a soma de todos os números de 1 até N

# 1. Receba esse número
n = int(input("Digite um número N: "))

# 2. Calcule a soma de 1 até N
soma = 0
for i in range(1, n + 1):
    soma += i
    print(f"Adicionando {i}, soma atual: {soma}")

# 3. Exiba o resultado na tela
print(f"A soma de 1 até {n} é: {soma}")
