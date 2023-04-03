from itertools import product
def prog1():
    words = product('егэ',repeat=5)
    k=0
    for w in words:
        word = ''.join(w)
        if (word[0]=='е') or (word[0]=='э'):
            k+=1
    print(k)
def prog2():
    words = 'егэ'
    k=0
    for i1 in words:
        for i2 in words:
            for i3 in words:
                for i4 in words:
                    for i5 in words:
                        word = i1+i2+i3+i4+i5
                        if word[0]=='е' or word[0]=='э':
                            k+=1
    print(k)
prog1()
prog2()