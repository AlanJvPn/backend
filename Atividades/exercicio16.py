# Dado um array de inteiros meu_array, um inteiro sortudo é um inteiro que tem uma frequencia no array igual ao seu valor.

meu_array = [1,2,3,3,4,4,5,6,7,1,2]

# 1. Criar um dicionário para adicionar todos os valores, descobrindo, assim, as chaves e valores

dicionario = {}


for i in meu_array:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1

print(dicionario)

# 2. Fazer um loop dentro do dicionario e descobrir quem é a chave que é igual ao valor

for chave, valor in dicionario.items():
    if chave == valor:
        print(f"Os Números sortudos são {chave}")