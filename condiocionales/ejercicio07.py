






base = int(input ('ingresa la base:'))
exponente =int(input( ingresa el exponente: ''))

if exponente >0:
    print(f'el numero {base} elevado a la {exponente} es {base ** exponente} ')
elif exponente == 0:
    print(f'el numero {base} elevado a la 0 es 1')
else:
    print(f'el numero {base} elevado a la {exponente} es 1/ {base}^{abs {exponente}}')
    