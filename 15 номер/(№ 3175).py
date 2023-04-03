def f(x, a):
    return ((190 % a == 0) and ((x % a != 0) and (x % 15 == 0)) <= (x % 75 != 0))

for a in range (1, 1000):
    flag = True
    for x in range(1, 1000):
        if f(x, a) == False:
            flag = False
            break
    if flag == True:
        print(a)