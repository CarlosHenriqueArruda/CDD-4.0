#Esse codigo pega uma lista pré definida e organiza ela retirando os numeros repetidos#
lista = [1,2,2,3,4,4,5,3,6,7,6,8]
'''novalista = []
def organizador(lista):
    for x in lista:
        if x not in novalista:
            novalista.append(x)
    print(novalista)
organizador(lista)'''
#Utilizando uma função do python que limpa e cria uma nova lista#
def organizador(lista):
    return list(set(lista))
resposta = organizador(lista)
print(resposta)