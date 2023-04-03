for i in range(2, 20):
    x = 87
    x1 = x
    s = ''
    while x>0:
        s = str(x%i) + s
        x = x//i
    if len(s) <= 2 and s[len(s)-1] == '2':
        print(i)
        print(x1, s)
