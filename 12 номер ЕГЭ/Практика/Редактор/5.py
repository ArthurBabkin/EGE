x = '3' + '6'*115 + '3'
while '63' in x or '664' in x or '6665' in x:
    if '63' in x:
        x = x.replace('63', '4', 1)
    elif '664' in x:
        x = x.replace('664', '65', 1)
    elif '6665' in x:   
        x = x.replace('6665', '63', 1)
print(x)