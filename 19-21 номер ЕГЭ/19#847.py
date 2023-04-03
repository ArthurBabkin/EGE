def win(s, k):
    if k==4 and s>=34:
        return True
    if k==4 and s<34:
        return False
    if k!=4 and s>=34:
        return False
    if k==3 or k==1:
        return win(s+1, k+1) or win(s+2, k+1) or win(s+3, k+1) or win(s*2, k+1)
    if k==2:
        return win(s + 1, k + 1) and win(s + 2, k + 1) and win(s + 3, k + 1) and win(s * 2, k + 1)

for i in range(1, 34):
    if win(i, 1):
        print(i)