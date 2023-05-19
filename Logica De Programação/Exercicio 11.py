#Peça duas notas de um aluno e mostre a media, mas se digitado menos de 0 e mais de 10, não aceite e peça novamente:#
#Codigo anterior alterado, dessa vez ele perguntar se o usuario deseja continuar#
continuar = "SIM"
while continuar == "SIM":
    N1 = float(input("Escreva a primeira nota: "))
    while N1 < 0 or N1 > 10:
        N1 = float(input("Número inválido, digite novamene: "))
    #########
    N2 = float(input("Escreva a segunda nota: "))
    while N2 < 0 or N2 > 10:
        N2 = float(input("Número inválido, digite novamente: "))
    print(f' A media do aluno é {(N1+N2)/2}')
    continuar=str(input("Deseja continuar? se sim, digite ´SIM´, se não, digite ´NÃO´: ")).upper()


