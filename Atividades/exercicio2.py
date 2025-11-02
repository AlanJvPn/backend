# Par ou ímpar: Receba um número e xiba se é par ou ímpar

# 1. Receba esse número
numero = int(input("Digite um número: "))

# 2. Verifique se é par ou ímpar
resultado = ""
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"
    
# 3. Exiba o resultado na tela
print(f"O número {numero} é {resultado}.")