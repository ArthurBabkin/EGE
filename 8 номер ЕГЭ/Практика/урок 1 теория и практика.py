from itertools import product
words = product('absx',repeat=5)
k=0
for i in words:
    word = ''.join(i)
    if (word[4]=='x' and word.count('x')==1 ) or (word.count('x')==0):
        k+=1
print(k)