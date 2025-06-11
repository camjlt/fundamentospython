print("soy una funcion")
print()
number = int('15')
longitud = len("hello")
my_str = str(26)

##funciones en phython
'''
def name(args):
    return
'''

def saludo():
    print('helloooooo!')

def cuenta_diez():
    for i in range(10):
        print(i, end= '-')
    print()

saludo()
saludo()
cuenta_diez()


def salusa_a(name):
    print('hello', name)

    saluda_a('peter')
    saluda_a('tony')
    saluda_a('bruce') 

    def reverse(name):
        print(name[::-1])

reverse('francisco')
reverse('universidad')
reverse('EVND')

def suma (num1,num2):
    resultado = num1 + num2
    return resultado

resultado = suma(23, 26)
print(resultado)

def resta(num1, num2)
    return num1 - num2

resultado = resta(23, 26)
print(resultado)