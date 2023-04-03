x = 216**6 + 216**4 + 36**6 - 6**14 - 24
s = ''
k = set()
while x > 0:
    s = str(x%6) + s
    k.add(str(x%6))
    x = x//6
print(k)
