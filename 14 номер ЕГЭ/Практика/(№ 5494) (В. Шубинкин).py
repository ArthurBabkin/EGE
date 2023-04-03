print('x, y, res')
for x in '0123456789ABCDEFG':
    for y in '0123456789ABCDE':
        res = int('123' + y + '5', 15) + int ('67' + x + '9', 17)
        if res%131==0:
            print(x, y, res/131)