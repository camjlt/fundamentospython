import random

numbers = []

for i in range(10):
   numbers.append(random.randint(1,10))

for number in numbers:
   print(number, number ** 2, number ** 3)
