from itertools import product
words = product('обществ', repeat=5)
k=0
for i in words:
    word = ''.join(i)
    if (word[0]!='щ') and (word[0]!='б') and (word[3:]=='вв') and ('ве' not in word) and ('ев' not in word) and ('тб' in word):
        k+=1
print(k)