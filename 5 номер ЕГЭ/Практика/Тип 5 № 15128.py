for i in range(1000, 10000):
    itog = ''
    i = str(i)
    k1 = int(str(i[0]) + str(i[1]))
    k2 = int(str(i[1]) + str(i[2]))
    k3 = int(str(i[2]) + str(i[3]))
    i = int(i)
    if k1>k2 and k1>k3 and (k2>k3 or k2==k3):
        itog = str(k2)+str(k1)
    elif k1>k2 and k1>k3 and k3>k2:
        itog = str(k3)+str(k1)
    elif k2>k1 and k2>k3 and (k1>k3 or k1==k3):
        itog = str(k1)+str(k2)
    elif k2>k1 and k2>k3 and k3>k1:
        itog = str(k3)+str(k2)
    elif k3>k1 and k3>k2 and (k1>k2 or k1==k2):
        itog = str(k1)+str(k3)
    elif k3>k1 and k3>k2 and k2>k1:
        itog = str(k2)+str(k3)
    elif k1==k2 and k3 == min(k1, k2, k3):
        itog = str(k1)+str(k2)
    elif k2==k3 and k1 == min(k1, k2, k3):
        itog = str(k2)+str(k3)
    elif k1==k3 and k2 == min(k1, k2, k3):
        itog = str(k1)+str(k3)
    elif k1==k2 and k1==k3:
        itog = str(k1)+str(k2)

    if int(itog)%2==0:
        print(i)
    if int(itog) == 1315:
        print('siu')
        print(i)