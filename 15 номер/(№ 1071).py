for a in range(0, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((5*y + 3*x != 110) or (x > a) or (2*y >a)) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)