for A in range(0, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 2*x != 99) or (y > A) or (x > A)) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)