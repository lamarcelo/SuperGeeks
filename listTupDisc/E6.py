lista = []

for x in range(5):
    lista.append(str(input('Digite um nome: \n')))

print('Lista fora de ordem: %s' % lista)
print('Lista em ordem: %s' % sorted(lista))