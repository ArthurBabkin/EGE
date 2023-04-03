from itertools import product
words = product('размах', repeat = 6)
k=set()
for w in words:
    word = ''.join(w)
    if (word.count('р') + word.count('з') + word.count('м') + word.count('х') >= 3):
        k.add(word)
print(len(k))