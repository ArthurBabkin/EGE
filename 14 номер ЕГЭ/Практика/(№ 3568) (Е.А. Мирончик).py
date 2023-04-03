def item16(k):
    s = ''
    while k>0:
        s = str(k%16) + s
        k = k//16
    if s[1] == '7':
        return True

def item8(k):
    s = ''
    while k > 0:
        s = str(k % 8) + s
        k = k // 8
    if s[0] == '5' and s[2] == '6':
        return True

def item4(k):
    s = ''
    while k > 0:
        s = str(k % 4) + s
        k = k // 4
    if s[3] == '1':
        return True

for i in range(20, 1000):
    if item16(i) == True and item8(i) == True and item4(i) == True:
        print(i)