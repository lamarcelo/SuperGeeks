Turma = str(input('Em qual turno você estuda? ( M-matutino | V-vespertino | N-noturno \n'))

if Turma == 'M' or Turma == 'M-matutino':
    print('Bom dia!')
elif Turma == 'V' or Turma == 'V-vespertino':
    print('Boa tarde!')
elif Turma == 'N' or Turma == 'N-noturno':
    print('Boa noite!')
else:
    print('Valor inválido.')