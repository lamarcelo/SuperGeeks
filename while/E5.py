numero = 0
digitados = 0
soma = 0

while numero != 999:
    digitados = digitados + 1
    soma = soma + numero
    numero = int(input('Digite um número: \n'))
else:
    print('Quantidade de numeros digitados: ', digitados)
    print('Soma dos numeros digitados: ', soma)