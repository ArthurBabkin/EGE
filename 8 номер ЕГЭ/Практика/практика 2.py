from itertools import product
words = product('моисей', repeat = 4)
k=0
for w in words:
    word = ''.join(w)
    if (word[0] != 'й') and (word.count('о') + word.count('и') + word.count('е')>=1):
        k+=1
print(k)