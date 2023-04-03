x = 2019*'1' + 2019*'3'
while '111' in x:
    x = x.replace('111', '2', 1)
    x = x.replace('222', '3', 1)
    x = x.replace('333', '1', 1)
print(x)