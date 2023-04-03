for i in range(2, 10):
    x = 94
    s = ''
    while x > 0:
        s = str(x%i)+s
        x//=i
    if s[0] == '2' and s[1] == '3':
        print(i)
