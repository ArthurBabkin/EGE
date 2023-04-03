x = (77 + 7**77)*7**77 + 77 + 7**7
s = ''
while x > 0:
    s = str(x%7) + s
    x = x//7
print(s.count('1'))