from itertools import permutations
def prog1():
    words = permutations('аммиакат')
    k = set()
    for w in words:
        word = ''.join(w)
        if (word.count('аи')+word.count('аа')+word.count('иа') >= 1) or (word.count('мм')+word.count('мк')+word.count('мт') + word.count('км')+word.count('кт')+word.count('тм') + word.count('тк') >= 1):
            k.add(word)
    print(len(k))

def prog2():
    words = permutations('аммиакат')
    k = set()
    for w in words:
        word = ''.join(w)
        s = ''
        for i in word:
            if i in 'аи':
                s+='g'
            if i in 'мкт':
                s+='s'
        if 'gg' in s or 'ss' in s:
            k.add(word)
    print(len(k))
prog1()
prog2()

