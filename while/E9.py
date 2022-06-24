import random

tentativas = 0

while True:
    numero = int(input('Digite um número: \n'))
    aleatorio = random.randrange(0, 10)
    tentativas = tentativas + 1
    print(tentativas)
    if numero == aleatorio:
        print('Você acertou o número!\nTentativas: ', tentativas)
        break