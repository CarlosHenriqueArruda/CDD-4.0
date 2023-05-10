#Contador de números negativos#
cont = 0
for x in range (10):
    Numero = (int(input("Digite um número: ")))
    if Numero < 0:
        cont += 1
print(f'Foram encontrados {cont} numeros negativos!')