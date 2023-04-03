from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) * n

for i in range(2100):
    f(i)

print(f(2023)/f(2020))