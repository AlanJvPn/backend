nome = "Andre Marcos"
sobrenome = 'Oliveira'

apresentacao = "Olá, meu nome é " + nome + ' ' + sobrenome +"."
print(apresentacao)

print("===============================")

apresentacao2 = f"Olá, meu nome é {nome} {sobrenome}."
print(apresentacao2)

print("===============================")

email = "andre.oliveira@gmail.com"
print(email)

print("0 :"+ email[0])
print("14 :"+ email[14])

print("Ultimo caracter: " + email[-1])
print("Penultimo caracter: " + email[-2])

email_usuario = email[0:14]
print("Email usuario: " + email_usuario)

email_dominio = email[15:len(email)]
print("Email dominio: " + email_dominio)

print("===============================")

print("Tamanho do email: " + str(len(email)))

print("Primeiros 5 caracteres: " + email[0:5])

print("@" in email)

print("===============================")

endereco = "Rua dos Andradas, 1000, Centro - Porto Alegre - RS"
print(endereco)

print(endereco.upper())

posicao = endereco.find("Centro")
print("Posição do Centro: " + str(posicao))

print(endereco.replace("Porto Alegre", "São Paulo"))

print(endereco.split(","))  # Divide a string em uma lista, usando a vírgula como separador

print("===============================")

idade = 30
print(type(idade))

idade = str(idade)
print(type(idade))

faturamento = "R$ 35 milhões"
print(faturamento)
print(type(faturamento))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))

print("===============================")

latlong = "-30.033158;-51.230200"
print(latlong)

posicao_ponto_virgula = latlong.find(";")
print("Posição do ponto e vírgula: " + str(posicao_ponto_virgula))

latitude = latlong[0:posicao_ponto_virgula]
print("Latitude: " + latitude)

longitude = latlong[posicao_ponto_virgula + 1:len(latlong)]
print("Longitude: " + longitude)