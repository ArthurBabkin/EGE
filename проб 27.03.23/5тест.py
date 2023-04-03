i = 3999
i = str(i)
s1 = 0
s2 = 0

for y in range(0, len(i)):
    if int(i[y]) % 2 == 0:
        s1 += int(i[y])
    elif int(i[y]) % 2 == 1:
        s2 += int(i[y])
print(s1, s2)
r = abs(s1-s2)
print(r)
if r == 30:
    print(i)