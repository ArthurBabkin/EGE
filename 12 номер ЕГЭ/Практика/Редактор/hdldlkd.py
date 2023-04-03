len1 = 1000000000
min = 10000000000

for i in range(101, 2000):
    x = '1' * i
    while '111' in x:
        x = x.replace('111', '2', 1)
        x = x.replace('2222', '333', 1)
        x = x.replace('33', '1', 1)
    if x.count('1') == 0:
        print(i)