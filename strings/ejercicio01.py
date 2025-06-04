my_string = input('ingresa un texto:')S

print(my_string)

for letra in my_string:
    print(letra, end= '-')

for index in range(len(my_string)):
    print(f'[{index}] = {my_string [index] }')

other_string = 'prueba'

print(other_string[0])
print(other_string[3])
print(other_string[5])