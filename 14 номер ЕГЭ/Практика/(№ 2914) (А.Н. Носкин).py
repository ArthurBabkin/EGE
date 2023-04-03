x = 2**51 + 2**40 + 2**35 + 2**17 - 2*5
s = ''
k = set()
while x > 0:
    s = str(x%16) + s
    x = x//16
for i in range(len(s)):
    k.add(int(s[i]))
print(k)
print(len(k))