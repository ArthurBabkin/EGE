for i in range(1, 10000000):
    x = 4**1014 - 2**i + 12
    x = str(bin(x)[2:])
    if x.count('0')==1000:
        print(i)