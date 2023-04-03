x = '5'*54+'7'
while '722' in x or '557' in x:
    if '722' in x:
        x = x.replace('722', '57', 1)
    else:
        x = x.replace('557', '72', 1)
print(x)