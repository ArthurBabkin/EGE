for x in range(1, 101):
    x1 = x
    x = x*'3'
    while '333' in x:
        x = x.replace('333', '4', 1)
        x = x.replace('4444', '3', 1)
    if x == '43':
        print(x1)