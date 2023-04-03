kol = 0
for i in range(1000, 10000):
    itog = ''
    if (int(str(i)[0])%2==1) and (int(str(i)[1])%2==1) and (int(str(i)[2])%2==1) and (int(str(i)[3])%2==1):
        first = int(str(i)[0]) + int(str(i)[1])
        second = int(str(i)[2]) + int(str(i)[3])
        if first > second:
            itog = str(second) + str(first)
        else:
            itog = str(first) + str(second)
        if int(itog) == 414:
            kol += 1
print(kol)