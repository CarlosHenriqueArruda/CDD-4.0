#Vai dividir 2 numeros, se o segundo numero for 0 ele não vai aceitar até que seja um numero diferente
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o o segundo numero: "))
while n2 ==0:
    print("por favor digite um numero maior que zero!")
    n2 = int(input("Digite o o segundo numero: "))
print(n1/n2)