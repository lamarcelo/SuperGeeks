P1 = float(input('Digite o valor do primeiro produto: \n'))
P2 = float(input('Digite o valor do segundo produto: \n'))
P3 = float(input('Digite o valor do terceiro produto: \n'))

menorP = P1

if P2 < menorP:
    menorP = P2
if P3 < menorP:
    menorP = P3

print('O produto mais barato custa: R$', menorP)