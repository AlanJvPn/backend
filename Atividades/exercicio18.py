meu_array = [elemento for elemento in range(1, 6)]
print(meu_array)

palavras = ["apple", "banana", "cherry", "date"]
iniciais = [palavra[0] for palavra in palavras]
print(iniciais)

# 1 2 3 4 5 6 7 8 9 10
# 1 4 9 16 25 36 49 64 81 100
quadrados_impares = [x**2 for x in range(1, 11) if x % 2 != 0]
print(quadrados_impares)  # Saída: [1, 9, 25, 49, 81]