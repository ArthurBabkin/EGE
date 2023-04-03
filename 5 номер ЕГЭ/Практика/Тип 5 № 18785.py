for i in range(100):
    n = bin(i)[2:]
    if int(n)%2==0:
        n1 = '1' + n + '0'
    elif int(n) % 2 == 1:
        n1 = '11' + n + '11'
    n1=int(n1, 2)
    if n1 > 52:
        print(i)
        break