# Dada um array de números inteiros, cada elemento aparece duas vezes, exceto um. Encontre ele.

num_inteiros = [1,1,2,2,3,3,4,5,5,6,6]

# 1. Criar um dicionário para adicionar os valores do array através de chave - valor.
dicionario = {}

for i in num_inteiros:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1

# 2. Fazer a verificação de qual valor aparece apenas uma vez
for chave, valor in dicionario.items():
    if valor == 1:
        print(f"O número {chave} aparece {valor} vezes.")