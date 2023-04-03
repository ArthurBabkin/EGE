minimum = 10000
for i in range(100, 2000):
    x = i*'1'
    while '1111' in x:
        x = x.replace('1111', '2', 1)
        x = x.replace('22', '11', 1)
    if x.count('1') < minimum:
        minimum = i
print(minimum)