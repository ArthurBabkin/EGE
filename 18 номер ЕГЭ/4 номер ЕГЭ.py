from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 1:
        return 2
    if n > 1:
        return (f(n - 1) + f(n - 2) + 2 * n + 4)
print(f(25))
