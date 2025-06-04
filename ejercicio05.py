full_name = input('escribe tu nombre completo: ')

word = full_name.split(' ')

initials = ''

for word in word:
   initials= word [0].upper()

print(initials)
