x = '1'*77
while '11111' in x:
    x = x.replace('222', '1', 1)
    x = x.replace('111', '1', 1)
print(x)