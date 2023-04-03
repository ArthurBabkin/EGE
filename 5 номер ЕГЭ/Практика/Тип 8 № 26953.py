from itertools import permutations
words = permutations('01234567', 5)
k=0
for w in words:
    e = ''.join(w)
    flag = True
    for i in range(len(e) - 1):
        if (e[0] == "0") or (int(e[i]) % 2 == 0 and int(e[i + 1]) % 2 == 0) or (
                int(e[i]) % 2 != 0 and int(e[i + 1]) % 2 != 0):
            flag = False
    if flag == True:
        k+=1
print(k)

