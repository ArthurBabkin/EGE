from itertools import permutations
t = 0
def perebor(n):
    pairs = set()
    n = str(n)
    pairs.add(n[0]+n[1])
    pairs.add(n[0]+n[2])
    pairs.add(n[1]+n[0])
    pairs.add(n[1]+n[2])
    pairs.add(n[2]+n[1])
    pairs.add(n[2]+n[0])
    permutations(pairs, 2)
    x = int(max(pairs)) - int(min(pairs))
    if x == 40:
        print('+')
        print(int(max(pairs)), int(min(pairs)))
        return(1)
    else:
        return(0)
    pairs.clear()

for i in range(900, 999):
    t += perebor(i)
print(t)