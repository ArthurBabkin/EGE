x = '6' * 282
while '222' in x or '6666' in x:
    if '222' in x:
        x = x.replace('222', '6', 1)
    else:
        x = x.replace('6666', '2', 1)
print(x)