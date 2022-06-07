I = str(input('Você tem irmãos(ãs)? \n'))

if I == "Sim" or I == "sim":
    Q = int(input('Quantos irmãos(ãs) você tem?: \n'))
    print('Que legal que você tem', Q, 'irmãos(ãs)!!')
else:
    G = str(input('Você gostaria de ter irmãos(ãs)? \n'))
    if G == "Sim" or G == "sim":
        print('Pede pra mamãe e pro papai com carinho pra você ganhar um(a) irmãozinho(a)!')
    else:
        print('Que pena que você não quer irmãozinhos(as) ;-;')