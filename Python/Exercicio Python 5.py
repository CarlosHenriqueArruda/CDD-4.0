#Nesse exercicio, aprendi a usar o RETURN
nome=input("Digite o nome do produto: ")
qnt=float(input("Digite a quantidade do produto: "))
valor=float(input("Digite o valor do produto: "))

def conta(a,b):
    return a*b

print(f"Nome do produto: {nome}\nQuantidade: {qnt}\nValor: {valor}\nValor total: {conta(qnt,valor)}")