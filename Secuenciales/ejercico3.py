#################################################################3
# datos los catetos de un triangulo rectangulo, calcular su hipoenusa.
############################3#33#3


#hipotenusa **2 =cateto1 ** 2 + cateto2 ** 2


##el operador doble asterisco ** permite elevar un numero
##a una potencia n


##para operaciones matematicas avanzadas importamos 
## la libreira math 
import math

cateto1 = int('input(ingresa valor de cateto 1:'))
cateto2 = int (intpu('ingresa valor de cateto 2: '))

hipotenusa = math.sqrt(cateto1 ** 2  cateto2 ** 2)

print('la hipotensua del triangulo es: ' + str(hipotenusa))