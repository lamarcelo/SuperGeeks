N1 = int(input('Digite um número: \n'))
N2 = int(input('Digite um número: \n'))
N3 = int(input('Digite um número: \n'))

maiorN = N1
menorN = N1

if N2 > maiorN:
    maiorN = N2
elif N3 > maiorN:
    maiorN = N3

if N2 < menorN:
    menorN = N2
elif N3 < menorN:
    menorN = N3

print('Maior numero: ', maiorN)
print('Menor número: ', menorN)