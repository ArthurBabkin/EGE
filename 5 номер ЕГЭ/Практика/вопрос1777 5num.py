def prog(n):
    n = bin(n)[2:]                  #Перевод в 2 систему счисления
    n = n + n[len(n)-1]             #Дублирование последнего числа
    if n.count('1') % 2 == 0:       #Четное => +0, нечетное => +1
        n += '0'
    else:
        n += '1'

    if n.count('1') % 2 == 0:       #Четное => +0, нечетное => +1
        n += '0'
    else:
        n += '1'
    r = int(n, 2)
    if r > 80:
        return r

for i in range(15):
    print(prog(i))