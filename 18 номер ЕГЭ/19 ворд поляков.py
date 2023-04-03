def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (2 * f(n-1) + g(n-1) - 2*n)

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return (f(n-1) + 2*g(n-1) + n)

print(g(14) + f(14))
