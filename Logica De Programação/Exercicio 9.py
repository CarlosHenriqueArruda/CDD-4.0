#Verificador de senha correta"
tentativas = 2
senhacorreta = 123
contador = 0
senha = int(input("Digite a sua senha:"))
if senha == senhacorreta:
    print("Senha correta!")
###############
while senha != senhacorreta and contador < tentativas:
    print("Senha incorreta, tente novamente:")
    senha = int(input("Digite a sua senha:"))
    contador +=1
    if contador >= 2:
        print('Senha incorreta, tentativas finalizadas!')