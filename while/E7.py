total = 0
num = int(input('Digite um número: \n'))
x = num

while True:
    print('chegou aqui')
    if x == 0:
        print(total)
        break
    else:
        if x < 0:
            total = total + x
            x = x + 1
        else:
            x = x - 1
            total = total + x