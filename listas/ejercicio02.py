words = []
words2 = []

for i in range(5):
    words.append(input('ingresa una letra: '))
    words2.append('')

end = 5
for word in words:
    words2[end - 1] = word
    end -=1

print(words)
print(words2)