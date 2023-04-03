x = 12**34 + 7*12**26 - 3*12**16 + 2*12**5 + 552
k = set()
s = []
while x > 0:
    k.add(x % 12)
    s.append(x % 12)
    x = x // 12
print(s, k)