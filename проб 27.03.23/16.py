from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 3:
        return n
    if n>3:
        if n%2==0:
            return n + f(n-1)
        if n%2==1:
            return n*n + f(n-2)

for i in range(1, 2100):
    f(i)
k = 0
for n in range(1, 2000):
    if f(n) < 10**8:
        k += 1
print(k)