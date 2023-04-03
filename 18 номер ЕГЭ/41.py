from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)-2*g(n-1)

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)+g(n-1)+n

d = str(f(36))
print(g(36))
sum = 0
for i in range(len(d)):
    sum += int(d[i])
print(sum)