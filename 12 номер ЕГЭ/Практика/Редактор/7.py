x = '>' + 11*'1' + 12*'2' + 30*'3'
while '>1' in x or '>2' in x or '>3' in x:
    if '>1' in x:
        x = x.replace('>1', '22>', 1)
    if '>2' in x:
        x = x.replace('>2', '2>', 1)
    if '>3' in x:
        x = x.replace('>3', '1>', 1)
sum = 0
for i in range(len(x)-1):
    sum += int(x[i])    
print(sum)