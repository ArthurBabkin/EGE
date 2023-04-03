letters = 'abcx'
k=0
for i1 in letters:
    for i2 in letters:
        for i3 in letters:
            for i4 in letters:
                for i5 in letters:
                    word = i1+i2+i3+i4+i5
                    if ((word[4] == 'x') and (word.count('x')==1)) or (word.count('x')==0):
                        k+=1
print(k)

