P1 = str(input('Você telefonou para a vítima? \n'))
P2 = str(input('Esteve no local do crime? \n'))
P3 = str(input('Mora perto da vítima? \n'))
P4 = str(input('Devia algo para a vítima? \n'))
P5 = str(input('Já trabalhou com a vítima? \n'))

rC = 0
lista = []

if P1 == "Sim" or P1 == "sim":
    rC = rC + 1

if P2 == "Sim" or P2 == "sim":
    rC = rC + 1

if P3 == "Sim" or P3 == "sim":
    rC = rC + 1

if P4 == "Sim" or P4 == "sim":
    rC = rC + 1

if P5 == "Sim" or P5 == "sim":
    rC = rC + 1

if rC == 2:
    print('\n Você é considerado(a) suspeito(a)...')
    print('Respostas positivas: ', rC)
elif rC > 2 and rC < 5:
    print('\n Você é considerado(a) cúmplice...')
    print('Respostas positivas: ', rC)
elif rC == 5:
    print('\n Você é considerado(a) culpado(a)...')
    print('Respostas positivas: ', rC)
else:
    print('\n Você é considerado(a) inocente...')
    print('Respostas positivas: ', rC)