from itertools import product
words = product('еклост', repeat=5)
k=[]
for i in words:
    word = ''.join(i)
    k.append(word)
    if (word[0]=='с') and ('оо' in word):
        break
print(len(k))
print(k)