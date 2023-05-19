#Fomos desafiados pelo professor a fazer um jogo da forca, utilizando apenas logica e um pouco de conhecimento em phyton#
#Separei por etapas cada passo do jogo#

################ INICIO ################
from random import choice
print("-- Jogo da Forca --")
print("Advinhe o nome o Jungler")
lista = ["wukong", "sylas", "amumu", "sejuani", "elise", "Rammus", "Rengar", "Graves", "Maokai", "Gragas", "Viego","Qiyana", "Rek'Sai", "Hecarim", "Nidalle","XinZhao","Kha-Zix","Fiddlesticks","Udyr","Evelynn","Jarvan IV","Zac","Kayn","Lilia","Ivern","Ekko","Leesin","Shaco","MasterYi","Karthus","Diana","Talon","Nocturne","Poppy","Nunu","Neeko","Kindred","Bel'veth","Zed"]
palavra = choice(lista)

################ CONTADOR DE LETRAS ################
contador = 0
for x in palavra:
    contador+=1
print(f'A palavra tem {contador} letras')

################ RESPOSTA ################
resposta = []
for x in palavra:
    resposta.append(x)

################ TENTATIVAS ################
listaunder = []
for k in range(contador):
        listaunder.append("_")
print(listaunder)

################ CODIGO ################
tentativas = 0
while tentativas != 10:
    letra=str(input("Digite uma letra: "))
    if letra == palavra or listaunder == resposta:
        print("Parabens, você acertou!")
        break
    if letra in palavra:
        print(f"A palavra possue essa letra! você tem mais {9-tentativas} tentativas!")
        tentativas+=1
        for z in range(contador):
            if palavra[z] == letra:
                listaunder[z] = letra
        print(listaunder)
        print("(caso desejar sair, digite ´sim´, caso já saiba a resposta, basta digitar e veremos se está correta!)")
    if letra == "sim":
        break
    if listaunder == resposta:
        print("Parabens, você acertou!")
        break
    if not letra in palavra:
       print(f"A palavra não possue essa letra, você tem {10-tentativas} tentativas!")
       tentativas+=1
    print()
