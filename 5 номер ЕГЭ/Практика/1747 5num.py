def arr(n):
    n = bin(n)[2:]
    d = 0
    c = ''

    for i in reversed(n):
        if i == '1':
            d += 1
            break
        else:
            d += 1

    for i in range(len(n)-d):
        if n[i] == '1':
            c = c +'0'
        else:
            c = c +'1'

    for i in range(len(n)-d, len(n)):
        c = c + n[i]

    if int(c, 2) == 98:
        print(int(n, 2))

for i in range(256):
    arr(i)
