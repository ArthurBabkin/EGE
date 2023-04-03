for i in range(2, 10):
    x = i**25 - 2*i**13 + 10
    s = ''
    sum = 0
    while x > 0:
        s = str(x%i) + s
        x = x//i
    for w in range(len(s)):
        sum += int(s[w])
    if sum == 75:
        print(i)