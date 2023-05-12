alunos = int(input("Digite o número de alunos: "))
contador = 0
lista = 1
while lista <= alunos:
    notas = float(input("Digite as notas dos alunos em ordem:"))
    contador+=notas
    lista +=1
media = contador / alunos
print(media)
