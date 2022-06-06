listaN = []

for n in range(3):
    n = int(input('Digite um número: \n'))
    listaN.append(n)

listaN.sort(reverse = True)
print('Números em ordem decrescente:', listaN)