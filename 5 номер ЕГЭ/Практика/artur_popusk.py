def go(n):
    n1 = n
    d = ''
    c = 0
    while n1 != 0:
        d = sТип 5 № 35463tr(n1 % 6) + d
        n1 = n1 // 6
    d += d[len(d) - 1]
    for i in range(len(d)-1):
        g = len(d)-i-1
        c = c + int(d[i]) * (6**g)
    c += int(d[len(d)-1])
    c = bin(c)[2:]
    c += c[len(c)-1]
    if int(c, 2) < 344:
        print(n)
for i in range(1000):
    go(i)