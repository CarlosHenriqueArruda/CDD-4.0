#Esse codigo usando função irá ler quantas vogais tem em qualquer texto escrito#
print("- Verificar quantas vogais existem em uma palavra ou texto -")
texto = str(input("Digite: ")).lower()
def contar (a):
    vogais = ["a","e","i","o","u"]
    contador = 0
    for x in a:
        if x in vogais:
            contador+=1
    print(contador)
contar(texto)
