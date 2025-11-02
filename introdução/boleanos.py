verdadeiro = True
print(verdadeiro)

falso = False
print(falso)

print(type(verdadeiro))

print("===============================")

saldo = 200
saque = 100

executar_saque = saque <= saldo
print("Saque autorizado: " + str(executar_saque))

codigo = 1234
codigo_correto = 334
validar_codigo = codigo == codigo_correto
print("Código correto: " + str(validar_codigo))

print("===============================")

print(True | True)
print(True | False)
print(False | False)
print(False | True)

print("===============================")

print(True & True)
print(True & False)
print(False & False)
print(False & True)

print("===============================")

print(not True)
print(not False)

print("===============================")

idade = 19
sangue = 'O-'
filhos = 0
telefone = None
telefone_fixo = ''

print(bool(idade)
      , bool(sangue)
      , bool(filhos)
      , bool(telefone)
      , bool(telefone_fixo))

print("===============================")

usario = "Andre"
senha = "123456"

usuario_cadastro = "Andre Perez"
senha_cadastro = "456"

login = (usario == usuario_cadastro) & (senha == senha_cadastro)
print("Login realizado: " + str(login))