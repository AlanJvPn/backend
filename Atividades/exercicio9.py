# Dado um endereço de IP valido (IPv4), retorne uma versão ajustada desse endereço IP.
# Um endereço IP ajustado substitui cada ponto "." por "[.]".

# 1. Receber a sttring com nosso endereço IP
ip_original = input("Digite um endereço de IP: ")

# 2. Fazer a operação para substituir os pontos por parenteses e ponto
ip_ajustado = ""

for i in ip_original:
    if i == ".":
        ip_ajustado += "[.]"
    else:
        ip_ajustado += i

print(ip_ajustado)