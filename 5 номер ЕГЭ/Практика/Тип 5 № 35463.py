def shag2(n):
    if n.count('0')==n.count('1'):
        s = n + n[len(n)-1]
    elif n.count('0') > n.count('1'):
        s = n + '1'
    elif n.count('0') < n.count('1'):
        s = n + '0'
    return s

for i in range(1000):
    s = ''
    n=bin(i)[2:]
    n = shag2(n)
    n = shag2(n)
    n = int(shag2(n), 2)
    if i > 99 and n%4==0:
        print(i)
        break

