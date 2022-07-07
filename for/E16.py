listaM = []
listaF = []
listaG = []
for i in range(4):
  sexo = input('Digite seu sexo: \n')
  if sexo == 'M' or sexo == 'F':
    idade = int(input('Digite sua idade: \n'))
    if sexo == 'M':
      listaM.append(idade)
      listaG.append(idade)
    else:
      listaF.append(idade)
      listaG.append(idade)

print('\n Idade média masculina: ' + str(int(sum(listaM)/len(listaM))) + 'anos')
print('Idade média feminina: ' + str(int(sum(listaF)/len(listaF))) + 'anos')
print('Idade média geral: ' + str(int(sum(listaG)/len(listaG))) + 'anos')