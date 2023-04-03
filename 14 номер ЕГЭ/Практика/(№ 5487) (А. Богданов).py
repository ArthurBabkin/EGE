for i in range(1,14):
    k1 = '3364' + str(i)
    k2 = str(i) + '7946'
    k3 = '55' + str(i) + '87'
    s1 = 0
    s2 = 0
    s3 = 0
    k = 1
    for w in range(len(k1)):
        s1 = s1 + int(k1[len(k1) - k]) *  11**w
        k += 1
    k = 1
    for w in range(len(k2)):
        s2 = s2 + int(k2[len(k2) - k]) * 12**w
        k += 1
    k = 1
    for w in range(len(k3)):
        s3 = s3 + int(k3[len(k3) - k]) * 14**w
        k += 1
    if s1 + s2 == s3:
        print(s3)