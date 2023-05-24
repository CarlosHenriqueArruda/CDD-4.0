# Fomos desafiados pelo professor a fazer um jogo da velha. #
# Utilizando apenas logica e um pouco de conhecimento em phyton #
# Separei por etapas cada passo do jogo #
print("Bem vindo ao jogo da velha! você jogará inicialmente contra o computador, aguarde novas atualizações!")
print("Nesse jogo você será o ´X´, e escolherá uma posição no tabuleiro abaixo.")
print("Cada posição está numerada para facilitar a sua gameplay, digite o numero na posição que deseja, boa sorte!")
import random
topo =["0","1","2"]
mid = ["3","4","5"]
bot = ["6","7","8"]
print(topo)
print(mid)
print(bot)
reiniciar = "restart"
while reiniciar == "restart":
    posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    while True:
        posicao = input("Escolha uma posição: ")
        if posicao.isdigit() and 0 <= int(posicao) <= 8:
            if posicao in posicoes_disponiveis:
                for x in range(3):
                    if posicao == topo[x]:
                        topo[x] = "[X]"
                    if posicao == mid[x]:
                        mid[x] = "[X]"
                    if posicao == bot[x]:
                        bot[x] = "[X]"
                print(topo)
                print(mid)
                print(bot)
                posicoes_disponiveis.remove(posicao)
                ################# Verificador de Vitoria HORIZONTAL #################

                contador = 0
                for x in topo:
                    if x == "[X]":
                        contador += 1
                if contador == 3:
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                contador = 0
                for x in mid:
                    if x == "[X]":
                        contador += 1
                if contador == 3:
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                contador = 0
                for x in bot:
                    if x == "[X]":
                        contador += 1
                if contador == 3:
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break

                ################# Verificador de Vitoria VERTICAL #################

                if topo[0] == "[X]" and mid[0] == "[X]" and bot[0] == "[X]":
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                if topo[1] == "[X]" and mid[1] == "[X]" and bot[1] == "[X]":
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                if topo[2] == "[X]" and mid[2] == "[X]" and bot[2] == "[X]":
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break

                ################# Verificador de Vitoria DIAGONAL #################

                if topo[0] == "[X]" and mid[1] == "[X]" and bot[2] == "[X]":
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                if topo[2] == "[X]" and mid[1] == "[X]" and bot[0] == "[X]":
                    print("Parabens, você venceu!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break

                ################# Verificador de EMPATE #################

                if len(posicoes_disponiveis) == 0:
                    print("Empate!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break

                ################ COMPUTADOR ###############
                posicao_computador = random.choice(posicoes_disponiveis)
                for i in range(3):
                    if posicao_computador == topo[i]:
                        topo[i] = "[O]"
                    if posicao_computador == mid[i]:
                        mid[i] = "[O]"
                    if posicao_computador == bot[i]:
                        bot[i] = "[O]"
                posicoes_disponiveis.remove(posicao_computador)
                print("O computador fez o movimento!")
                print(topo)
                print(mid)
                print(bot)
                ################# Verificador de Vitoria VERTICAL COMPUTADOR #################

                if topo[0] == "[O]" and mid[0] == "[O]" and bot[0] == "[O]":
                    print("Parabens, você perdeu para um computador aleatorio!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                if topo[1] == "[O]" and mid[1] == "[O]" and bot[1] == "[O]":
                    print("Parabens, você perdeu para um computador aleatorio!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                if topo[2] == "[O]" and mid[2] == "[O]" and bot[2] == "[O]":
                    print("Parabens, você perdeu para um computador aleatorio!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break

                ################# Verificador de Vitoria DIAGONAL COMPUTADOR #################

                if topo[0] == "[O]" and mid[1] == "[O]" and bot[2] == "[O]":
                    print("Parabens, você perdeu para um computador aleatorio!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break
                if topo[2] == "[O]" and mid[1] == "[O]" and bot[0] == "[O]":
                    print("Parabens, você perdeu para um computador aleatorio!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break

                ################# Verificador de EMPATE COMPUTADOR #################

                if len(posicoes_disponiveis) == 0:
                    print("Empate!")
                    reiniciar = input("Digite 'restart' para jogar novamente ou qualquer outra tecla para sair: ")
                    if reiniciar == "restart":
                        topo = ["0", "1", "2"]
                        mid = ["3", "4", "5"]
                        bot = ["6", "7", "8"]
                        posicoes_disponiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                        print(topo)
                        print(mid)
                        print(bot)
                    else:
                        break

            else:
                print("Essa posição não está disponivel, tente outra!")
        else:
            print("Digite apenas numeros de 0 a 8 correspondentes a posição que deseja preencher!")