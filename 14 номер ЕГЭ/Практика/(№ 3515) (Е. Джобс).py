x = 43*7**103 - 21*7**57 + 98
k = []
s = ''
while x > 0:
    s = str(x%7) + s
    x = x//7
for i in range(len(s)):
    k.append(int(s[i]))
print(sum(k))

