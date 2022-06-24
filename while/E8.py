soma = 0
x = 0

while True:
    n = int(input("Digite um número:\n"))
    if n >= 10:
        while x < n:
            x = x + 2
            soma += x
        print(soma)
        break