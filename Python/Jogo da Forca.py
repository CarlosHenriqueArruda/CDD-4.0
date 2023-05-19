from random import choice
################ INICIO ################
print("-- Jogo da Forca --")
print("Advinhe o nome o Jungler")
lista = ["wukong", "sylas", "amumu", "sejuani", "elise", "Rammus", "Rengar", "Graves", "Maokai", "Gragas", "Viego","Qiyana", "Rek'Sai", "Hecarim", "Nidalle","XinZhao","Kha-Zix","Fiddlesticks","Udyr","Evelynn","Jarvan IV","Zac","Kayn","Lilia","Ivern","Ekko","Leesin","Shaco","MasterYi","Karthus","Diana","Talon","Nocturne","Poppy","Nunu","Neeko","Kindred","Bel'veth","Zed"]
palavra = choice(lista)
print(palavra)

################ CONTADOR DE LETRAS ################
contador = 0
for x in palavra:
    contador+=1
print(f'A palavra tem {contador} letras')
print( f"_ "*contador)

################ TENTATIVAS ################
tentativas = 0
while tentativas != 10:
    letra=str(input("Digite uma letra: "))
    if letra in palavra:
        print(f"A palavra possue essa letra! você tem mais {10-tentativas} tentativas!")
        tentativas+=1
    else:
       print(f"A palavra não possue essa letra, você tem {10-tentativas} tentativas!")
       tentativas+=1
