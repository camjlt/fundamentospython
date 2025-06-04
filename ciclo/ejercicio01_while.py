numero = int(input('ingresa un numero para calcular su factorial: '))

factorial = 1 

while numero > 1:
    factorial = factorial * numero
    numero = nuumero -1

print('el resultado es:', factorial)