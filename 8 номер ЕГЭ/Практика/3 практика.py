from itertools import permutations
words = permutations('ареал')
k=set()
for w in words:
    word = ''.join(w)
    if (word.count('еа') == 0) and (word.count('ае') == 0) and (word.count('аа') == 0):
        k.add(word)
print(len(k))