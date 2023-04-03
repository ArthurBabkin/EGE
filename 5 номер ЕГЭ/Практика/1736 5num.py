def arr(n):
    n = bin(n)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    if int(n, 2) > 108:
        print(int(n, 2))

for i in range (1000):
    arr(i)
