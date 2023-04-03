from itertools import product
words = product('polygon', repeat = 5)
k=0
for i in words:
    word = ''.join(i)
    if (word[2]=='o' or word[2]=='y') and (word[0]==word[4]) and (word[1]==word[3]):
        k+=1
print(k)