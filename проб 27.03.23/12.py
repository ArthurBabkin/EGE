min = 100000000
d = 1000000
for i in range(101, 1000):
    z = 1 * i
    x = '1' * i
    while '111' in x:
        x = x.replace('111', '2', 1)
        x = x.replace('2222', '333', 1)
        x = x.replace('33', '1', 1)
    if min > x.count('1') and d > z and x.count('1') > 0:
        min = x.count('1')
        d = z


print(min)
print(d)