from itertools import product
ss = set()
for n in set(product('КОМПЬЮТЕР', repeat = 6)):
    n = ''.join(n)
    if n.find('К') >= 0 and n.rfind('Т') >= 0:
        for j in range(n.find('К')+1, n.rfind('Т')):
            if n[j] == '0':
                ss.add(n)

print(len(ss))