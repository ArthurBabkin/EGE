x = '1' + '0'*75
while '10' in x or '1' in x:
    if '10' in x:
        x = x.replace('10', '001', 1)
    else:
        x = x.replace('1', '00', 1)
print(x.count('0'))