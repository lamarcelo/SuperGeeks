P1 = str(input('Você telefonou para a vítima? \n'))
P2 = str(input('Esteve no local do crime? \n'))
P3 = str(input('Mora perto da vítima? \n'))
P4 = str(input('Devia algo para a vítima? \n'))
P5 = str(input('Já trabalhou com a vítima? \n'))

rC = 0
lista = []

if P1 == "Sim" or P1 == "sim":
    lista.append("Sim")
else:
    lista.append("Não")

if P2 == "Sim" or P2 == "sim":
    lista.append("Sim")
else:
    lista.append("Não")

if P3 == "Sim" or P3 == "sim":
    lista.append("Sim")
else:
    lista.append("Não")

if P4 == "Sim" or P4 == "sim":
    lista.append("Sim")
else:
    lista.append("Não")

if P5 == "Sim" or P5 == "sim":
    lista.append("Sim")
else:
    lista.append("Não")

for x in lista:
    if x == "Sim":
        rC = rC + 1

if rC == 2:
    print('Você é considerado(a) suspeito(a)...')
    print('Respostas positivas: ', rC)
elif rC > 2 and rC < 5:
    print('Você é considerado(a) cúmplice...')
    print('Respostas positivas: ', rC)
elif rC == 5:
    print('Você é considerado(a) culpado(a)...')
    print('Respostas positivas: ', rC)
else:
    print('Você é considerado(a) inocente...')
    print('Respostas positivas: ', rC)