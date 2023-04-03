from itertools import product
words = product('аттестат', repeat = 8)

for i in words:
    word = ''.join(i)
print(word)
