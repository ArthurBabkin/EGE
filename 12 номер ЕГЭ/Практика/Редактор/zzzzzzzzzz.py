x = '1' * 101
while '111' in x:
    x = x.replace('111', '2', 1)
    x = x.replace('2222', '333', 1)
    x = x.replace('33', '1', 1)
x1 = '1' * 111
while '111' in x1:
    x1 = x1.replace('111', '2', 1)
    x1 = x1.replace('2222', '333', 1)
    x1 = x1.replace('33', '1', 1)
print(x, x1)