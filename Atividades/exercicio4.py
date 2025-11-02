# Tabuada: Receba um número e exiba a tabuada desse número de 1 a 10

# 1. Receba esse número
numero = int(input("Digite um número para ver a tabuada: "))

# 2. Gere a tabuada
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")