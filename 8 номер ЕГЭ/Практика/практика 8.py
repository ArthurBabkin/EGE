from itertools import product
words = product('012345678', repeat=5)
k=0
for i in words:
    word = ''.join(i)
    if (word[0] not in '01357') and (word[-1] not in '18') and (word.count('3')<=1):
        k+=1
print(k)