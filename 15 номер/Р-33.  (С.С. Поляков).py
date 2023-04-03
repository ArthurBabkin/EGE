for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y - x != 5) or (a < 2 * x**3 + y) or (a < y**2 +16)) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)