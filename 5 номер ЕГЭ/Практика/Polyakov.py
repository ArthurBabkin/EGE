def item8(m):
    m = int(m)
    s = ''
    while m>0:
        s1 = str(m%8)
        s = s1 + s
        m = m//8
    if s[len(s) - 1] == '4':
        return True
k=0

for i in range(1000, 10000):
    n = str(i)
    if int(n[0])%4==0:
        n = '9' + n[1:]
    elif int(n[0])%2==0 and int(n[0])%4!=0:
        n = '3' + n[1:]

    if (n[0]=='9') and (item8(n)== True):
        k+=1
print(k)