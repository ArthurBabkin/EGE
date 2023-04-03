def Del(x, a):
    return ((70 % a == 0) and ((x % a == 0) or ((x * 35 != 0) or (x % 63 != 0))))
for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(Del(x, a)) == True:
            flag = False
    if flag == True:
        print(a)
