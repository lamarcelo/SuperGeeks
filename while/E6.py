while True:
    numero1 = int(input('Digite um número: \n'))
    numero2 = int(input('Digite um número: \n'))

    print('Soma dos numeros digitados: ', numero1 + numero2)

    pergunta = str(input('Deseja fazer outra soma?\n'))
    if pergunta == 'sim':
        print('Retornando para uma nova soma...')
    else:
        break