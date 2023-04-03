from itertools import product
words = product('дкмо', repeat=5)
k=[]
for i in words:
    word = ''.join(i)
    k.append(word)
print(k.index('комод')-k.index('домок')+1)
print(k)