pesos = []
idades = 0

for i in range(7):
    idade = int(input('Digite sua idade: \n'))
    peso = int(input('Digite seu peso: \n'))
    pesos.append(peso)
    idades = idades + idade

    if i == 6:
        maior90 = [x for x in pesos if x >= 90]
        print('\nMaiores que 90KG:', len(maior90))
        print('\nIdade media:', round((idades/7),2))
