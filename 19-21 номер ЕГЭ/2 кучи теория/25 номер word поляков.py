win = 55
start = 9
def f(a, b, c, m):
    if a + b >= win:
        return m % 2 == c % 2
    if m == c:
        return False
    moves = [f(a + 2, b, c + 1, m),
             f(a, b + 2, c + 1, m),
             f(a, b * 2, c + 1, m),
             f(a * 2, b, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)
for s in range(1, 46):
    for m in range(1, 4 + 1):
        if f(start, s, 0, m) == True:
            print(s, m)