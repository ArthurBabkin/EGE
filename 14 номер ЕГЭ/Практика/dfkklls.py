x = 8* 343 ** 5 + 9 * 49**8 - 48
s = ''
while x > 0:
    s = str(x%7) + s
    x = x // 7
print(s.count('6'))
    