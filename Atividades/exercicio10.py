# Dado um array de números inteiros, retorne quantos deles contêm um número par de dígitos.
# nums = [12,345,2,6,7896]
# novo_array = ["12", "345", "2", "6", "7896"]

# 1. Criar um novo array de strings que vai ter os mesmos valores do primeiro array, porem como strings
novo_array = ["12", "345", "2", "6", "7896"]
contagem = 0
# 2. Fazer um looping dentro do novo_array para fazer a verificação de números com digiros pares
for i in novo_array:
    if len(i) % 2 == 0:
        contagem += 1

# 3. Fazer a contagem e mostrar na tela o resultado
print(f"O total de números pares dessa lista são {contagem}:")