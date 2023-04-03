def win1(s):
    if 2*s>=29 or s + 1 >= 29:
        return True
    else:
        return False
for s in range(1, 29):
    if win1(2*s) or win1(s+1):
        print(s)