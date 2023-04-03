from itertools import product
numbers = product('01234567', repeat=5)
k=0
for i in numbers:
    number = ''.join(i)
    if number[0]!='0' and number.count('6')==1 and '16' not in number and \
        '16' not in number and '36' not in number and '56' not in number and \
        '61' not in number and '63' not in number and '65' not in number and \
        '76' not in number and '67' not in number:
            k+=1
print(k)