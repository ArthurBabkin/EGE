from itertools import product
words = product('апрсу', repeat=3)
k=[]
for i in words:
    word = ''.join(i)
    k.append(word)
    if (word[0]=='с'):
        break
print(len(k))
