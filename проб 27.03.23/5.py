i = 0
r = 0
while r!=30:
    i = str(i)
    s1 = 0
    s2 = 0
    for y in range(0, len(i)):
        if y % 2 == 0:
            s1 += int(i[y])

        elif y % 2 == 1:
            s2 += int(i[y])

    r = abs(s1 - s2)

    if r == 30:
        print(i)
        break
    i = int(i) + 1



