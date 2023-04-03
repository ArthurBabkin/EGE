x = 81
for i in range (2, 10):
    x=81
    s=''
    while x>0:
        s=str(x%i) + s
        x=x//i
    s = int(s)
    if s == 121:
        print(i)

