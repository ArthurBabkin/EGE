x = '5' *500
five = 0
while '555' in x or '333' in x:
    if '333' in x:
        x = x.replace('333', '5', 1)
    else:
        x = x.replace('555', '3', 1)
        five += 3
print(five)