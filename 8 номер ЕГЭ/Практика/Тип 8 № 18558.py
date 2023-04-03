from itertools import product
words = product('иван',repeat=5)
k = 0   
for i in words:
    word = ''.join(i)
    if (word.count('и')>=1):
        k+=1
print(k)