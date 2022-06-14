idades = []

for i in range(10):
    idade = int(input('Digite sua idade: \n'))
    idades.append(idade)

    if i == 9:
        maior18 = [x for x in idades if x >= 18]
        print('\nMaiores que 18 anos:', len(maior18))
