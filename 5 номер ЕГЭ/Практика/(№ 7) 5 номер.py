for i in range(1, 200):
    sum = 0
    r = str(bin(i)[2:])
    for j in range(len(r)-1):
        sum = (sum+int(r[j])) % 2
        if sum == 1:
            r = r + '1'
        elif sum == 0:
            r = r + '0'
    for j in range(len(r)-1):
        sum = (sum+int(r[j])) % 2
        if sum == 1:
            r = r + '1'
        elif sum == 0:
            r = r + '0'

    if int(r, 2) > 125:
        print(i)