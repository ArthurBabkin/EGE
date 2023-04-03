for i in range(3, 100):
    n = str(bin(i)[2:])
    n1 = n[:(len(n)-1)] + n[1] + n[1]
    n2 = int(n1, 2)
    if n2 > 76:
        print(i)
        break