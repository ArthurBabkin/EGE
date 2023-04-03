x = 9**8 + 3**5 - 9
s=''
while x>0:
    s= str(x%3) + s
    x = x//3
print(s.count('2'))