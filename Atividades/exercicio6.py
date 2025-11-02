# Inverter uma string: Receba uma string do usuário e exiba a string invertida.

# 1. Receba a string
string = input("Digite uma frase: ")

# 2. Inverta a string
string_invertida = string[::-1]
"""string[::-1] usa slice (fatiamento): sintaxe geral sequence[início:fim:passo].
Quando início e fim são omitidos e passo = -1, 
o slice percorre a sequência de trás pra frente, retornando uma nova string invertida."""

# 3. Exiba o resultado na tela
print(f"A string invertida é: {string_invertida}")