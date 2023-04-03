from itertools import product
from itertools import permutations
words = product('компьютер', repeat = 5)

k = set()
for i in words:
    word = ''.join(i)
    k.add(word)
s = 0
k1 = set()
for i in k:
    k1.clear()
    for y in range(0, 5):
        k1.add(i[y])
    if len(k1) >= 3:
        s += 1
print(s)