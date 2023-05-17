numero = int(input("Digite um numero: "))
def verificador(numero):
    if numero == 1:
        return numero, "Não é primo"
    elif numero == 2:
        return numero, "É primo"
    else:
        for x in range(2,numero):
            if numero % x == 0:
                return numero, "Não é primo"
        return numero, "É primo"
print(verificador(numero))