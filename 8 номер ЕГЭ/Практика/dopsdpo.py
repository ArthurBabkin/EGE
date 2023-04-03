from itertools import product
words = product('ьсоне', repeat = 4)
k =[]
for i in words:
    word = ''.join(i)
    k.append(word)
print(k[99])
print(k)

