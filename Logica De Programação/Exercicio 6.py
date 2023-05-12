#While = enquanto - condição (ex: enquanto tiver cadeiras, pode entrar)
lista = 1
contador = 0
while lista <=10:
    numero = float(input("Digite o valor:"))
    contador += numero
    media = contador / 10
    lista += 1
print(media)