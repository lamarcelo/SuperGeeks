numero = int(input('Digite o número máximo: \n'))
lista = []

for x in range(numero+1):
  lista.append(x)

if numero%2 != 0:
    lista.remove(0)
    print(*lista)
    for i in range(1, numero+1):
        if len(lista) > 1:
            lista.remove(max(lista))
            lista.remove(min(lista))
            print(*lista)