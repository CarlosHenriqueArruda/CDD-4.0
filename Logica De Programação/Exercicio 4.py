#Analizará quantos números estão entra 10 e 20!!#
var = 0
var2 = 0
for x in range (5):
    Numero = (int(input("Digite um número: ")))
    if Numero >= 10 and Numero <=20:
        var += 1
    else:
        var2 +=1

print(f'Foram encontrados {var} dentro do intervalo e {var2} fora do intervalo!!')