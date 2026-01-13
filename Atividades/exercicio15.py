# Dado um array meu_array contendo n números distintos no intervalo [0, n],
# retorne o único número no intervalo que está faltando no array.

meu_array = [0,1,3,4,5,6,7,8,9,10]
 

tamanho_array = len(meu_array)
print(tamanho_array)

soma_array = sum(meu_array)
print(soma_array)

soma_total = tamanho_array * (tamanho_array + 1) / 2

print(soma_total - soma_array)