import ramdom

aleatorio = random.randint(1, 100)
intentos = 10

while True:
    numero = int(input('adivina el numero: '))
    if aleatorio == numero:
        print('adivinaste el numero!')
        print(f'lo hiciste en {intentos} intentos')
        break
    elif numero > aleatorio:
        print('ingresa otro más pequeño: ')
        intentos = intentos - 1
    else:
        print('ingresa otro más grande: ')
        intentos = intentos - 1
    if intentos == 0: 
        print('perdiste!!') 
        break