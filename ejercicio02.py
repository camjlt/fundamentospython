calcular el area y perimetro de un rectangulo 



print ("programa que calcula area y perimetro de un rectangulo")

altura = input ('ingresa la altura:')
altura = int (altura)
base = int (input ('ingresa la base: '))

perimetro = base + altura + base + altura
area = base * altura 

print ("el area del rectangulo es: " + str (area))
print ("el perimetro del rectangulo es:" + str (perimetro))
