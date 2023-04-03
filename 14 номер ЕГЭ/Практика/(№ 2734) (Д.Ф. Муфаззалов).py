for i in range(4, 100):
    x = (88 + 2*8**i)*8**i + 88 + 8*8
    s = ''
    sum = 0
    while x>0:
        s = str(x%8) + s
        x //= 8
    print(s) 
    for w in range(len(s)):
        sum += int(s[w])
    print(sum)


