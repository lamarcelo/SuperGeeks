while True:
    nota = int(input('Digite a nota: \n'))
    if nota >= 0 and nota <= 10:
        print('Nota registrada.')
        break
    else:
        print('Nota inválida, digite a nota entre 0 e 10.')