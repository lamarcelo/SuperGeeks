D = int(input('Digite o dia de seu aniversário: \n'))
M = int(input('Digite o mês de seu aniversário: \n'))
A = int(input('Digite o ano de seu aniversário: \n'))

if D >= 1 and D <= 31:
    if M >= 1 and M <= 12:
        if A >= 1903 and A <= 2022:
            print('Você nasceu em ', D,"/", M,"/", A)
        else:
            print('Ano de seu aniversário é inválido.')
    else:
        print('Mês de seu aniversário é inválido.')
else:
    print('Dia de seu aniversário é inválido.')
