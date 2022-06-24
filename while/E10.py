import random

pedra = 0
papel = 1
tesoura = 2
jogar_novamente = "Sim"
vitoriasP = 0
vitoriasR = 0

while (jogar_novamente == "Sim"):
    if vitoriasP < 3:
        if vitoriasR < 3:
            jogador1 = int( input("0 - Pedra\n1 - Papel\n2 - Tesoura\nEscolha sua opção: " ))
            jogador2 = random.randrange(0, 2)
            if (0 <= jogador1 <= 2) and (0 <= jogador2 <= 2):
                if (jogador1 == jogador2):
                    print("Vish... Deu empate!\n" )
                elif (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
                    vitoriasP = vitoriasP + 1
                    print("Você ganhou e está com {} ponto(s)!\n".format(vitoriasP))
                else:
                    vitoriasR = vitoriasR + 1
                    print("O robo ganhou e está com {} ponto(s)!\n".format(vitoriasR))
            else:
                print("Opção inválida." )
        else:
            print('Você perder :( O robo ganhou 3 pontos e venceu de você!')
            break
    else:
        print('Você ganhou! Você ganhou 3 pontos e venceu do robo!')
        break