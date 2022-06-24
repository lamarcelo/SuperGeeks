import random

pedra = 0
papel = 1
tesoura = 2
jogar_novamente = "Sim"
while (jogar_novamente == "Sim"):
    jogador1 = int( input("0 - Pedra\n1 - Papel\n2 - Tesoura\nEscolha sua opção: " ))
    jogador2 = random.randrange(0, 2)
    if (0 <= jogador1 <= 2) and (0 <= jogador2 <= 2):
        if (jogador1 == jogador2):
            print("Vish... Deu empate!" )
        elif (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
            print("Você ganhou do robo!" )
        else:
            print("O robo ganhou :( Tente novamente!" )
    else:
        print("Opção inválida." )
    jogar_novamente = input("Você quer tentar novamente? " )