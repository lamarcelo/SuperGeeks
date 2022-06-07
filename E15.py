N1 = int(input('Digite um número: \n'))
N2 = int(input('Digite outro número: \n'))

Op = str(input('Que operação você deseja realizar com os números escolhidos? \n'))

operacoes = ['divisão', 'divisao', 'multiplicação', 'multiplicacao']

if Op in operacoes:
    if Op == 'divisao' or Op == 'divisão':
        print('A operação', N1, '%', N2, 'é igual a:', N1 / N2)
    else:
        print('A operação', N1, 'x', N2, 'é igual a:', N1 * N2)