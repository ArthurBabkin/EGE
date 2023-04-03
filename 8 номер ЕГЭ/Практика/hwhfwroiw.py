from itertools import product
from itertools import permutations
words = product('компьютер', repeat = 5)
k = set()
k1 = set()

for i in words:
    word = ''.join(i)
    k.add(word)

for i in k:
    words1 = permutations(i)
    for y in words1:
        word1 = ''.join(y)
        if word1[0] == word1[4] and word1[1] == word1[3]:
            k1.add(word1)
print(len(k1))