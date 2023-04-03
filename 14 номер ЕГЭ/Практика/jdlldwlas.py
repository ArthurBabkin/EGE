for i in range(1, 10):
    x = 87
    s = ''
    while x>0:
        s = str(x%i) + s
        x = x//i
    if len(s) <= 2 and s[len(s)-1] == '2':
        print(i)
