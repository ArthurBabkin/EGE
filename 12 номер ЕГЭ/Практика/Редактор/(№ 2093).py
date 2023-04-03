x = '>' + 14*'1' + 20*'2' + 25*'3'
while '>1' in x or '>2' in x or '>3' in x:
    if '>1' in x:
        x = x.replace('>1', '22>3', 1)
    if '>2' in x:
        x = x.replace('>2', '2>', 1)
    if '>3' in x:
        x = x.replace('>3', '11>2', 1)
sum = 0
for i in range(0, len(x)):
    if x[i] != '>':
        sum += int(x[i])
print(sum)