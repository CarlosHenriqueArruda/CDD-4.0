#Nesse codigo aprendi a utilizar a função "DEF" para definir uma função# Criei uma calculadora simples com menu de escolha#
opcao = 0
#################
def somar(n1,n2):
    soma = n1+n2
    print(f"O resultado da soma é: {soma}")
    print()
def subtrair(n1,n2):
    subtracao = n1-n2
    print(f"O resultado da subtração é: {subtrair}")
    print()
def multiplicar(n1,n2):
    multiplicacao = n1*n2
    print(f"O resultado da multiplicação é: {multiplicar}")
    print()
def dividir(n1,n2):
    dividisao = n1/n2
    print(f"O resultado da divisão é: {dividir}")
    print()
#################

while opcao != 5:
    escolha = int(input("Escolha uma opção: \n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair\nSua opção: "))
    print()
    if escolha == 1:
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        print()
        somar(a,b)
    if escolha == 2:
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        print()
        subtrair(a,b)
    if escolha == 3:
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        print()
        multiplicar(a,b)
    if escolha == 4:
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        print()
        dividir(a,b)
    if escolha == 5:
        break