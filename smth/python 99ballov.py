import math
x = 10
print(math.cos(math.pi/3))
print(math.factorial(7))
print(math.log10(100))
print(math.log(16,2))

#y = []
#or i in range(5):
#   y.append(int(input()))
#print(sum(y))

s = '321'
s1 = [1, '22', 3]
x1,x2,x3 = map(int, s)
print(x1, x2, x3)
print(sum(map(int, s1)))
print(sum(map(int, s)))

b = [1, 2, 3 ,5 ,4]
c = sorted(b)
b.sort()
print(b, c, sep='\n')

g = [1, 2, 6, 32, 4]
g1 = g.copy()
print(g1)