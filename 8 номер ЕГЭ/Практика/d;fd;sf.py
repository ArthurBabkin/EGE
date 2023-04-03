from itertools import permutations
words = permutations('тратата')
k=set()
for i in words:
    k.add(i)
print(len(k))