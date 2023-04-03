for i in '0123456789ABCDE':
    k1 = ['5', i, '3', '2', '1']
    k2 = ['3', '3', '2', i, '1']
    k11 = 0
    k22 = 0
    for j in range(0, 5):
        k11 += int(k1[j]) * 15 ** j
        k22 += int(k2[j]) * 15 ** j
    k3 = k11 + k22
    if k3 % 14==0:
        print(k3//14)

