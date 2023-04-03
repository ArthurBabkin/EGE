list1 = []
n=0

kol = int(input('Введите количество симоволов: '))

for i in range(kol):
    list1.append(int(input('Введите число: ')))

for i in range(kol-1):
    n+=1
    if list1[i]%2==0:
        print('Порядковый номер первого четного элемента - ', n)
        break

