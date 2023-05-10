#Função para verificar se o numero é positivo, negativo ou igual a zero
def verificar(a):
    if numero > 0:
        print("P")
    if numero < 0:
        print("N")
    if numero == 0:
        print("Z")
numero = int(input("Digite o numero: "))
verificar(numero)