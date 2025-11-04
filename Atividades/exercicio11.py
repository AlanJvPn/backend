# Você recebe um array de números inteiros num_inter.
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array.
# retorne a soma de todos os elementos únicos de num_inter.

num_inter = [1,2,3,3,3,3,4,4,5,5]

# 1. Criar um dicionário para adicionar a chave e o valor
dicionario = {}

for i in num_inter:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1

# 2. Encontrar quem são os valores que aparecem uma única vez
# 3. Fazer a soma das chaves que aparecem apenas 1 vez
soma_chaves = 0

for chave, valor in dicionario.items():
    if valor == 1:
        soma_chaves += chave

print(f"A Soma das chaves que aparecem apenas uma vez é {soma_chaves}: ")