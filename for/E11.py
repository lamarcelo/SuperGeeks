numero = int(input('Digite o número máximo: \n'))
lista = []
lista.append(range(numero+1))

if numero%2 != 0:
    for i in range(1, numero+1):
        if len(lista) > 1:
            print(lista)
            lista.remove(max(lista))
            lista.remove(min(lista))
            print(lista)