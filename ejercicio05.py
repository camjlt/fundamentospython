pharase = input('escribe una frase: ')
char= input('escribe una letra: ')

times = 0

for i in pharase:
    if char == pharase[1]:
        times += 1

print(f'la letra{char} se encuentra {times} veces !')