T = float(input('Qual a temperatura atual de onde você mora? \n'))

P1 = str(input('Gostaria de converter essa temperatura de Fahrenheit para Celsius? \n'))

if P1 == 'nao' or P1 == 'não':
    P2 = str(input('Gostaria de converter essa temperatura de Celsius para Fahrenheit? \n'))
    if P2 == 'sim':
        F = (T*9/5) + 32
        print('A temperatura', T, '°C equilave a', round(F,2), '°F')
elif P1 == 'sim':
    C = (T-32)*5/9
    print('A temperatura', T, '°F equilave a', round(C,2), '°C')
