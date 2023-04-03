for i in range(1, 100):
    for j in range(1, 100):
        for w in range(1, 100):
            s1 = '0' + i*'1' + j*'2' + w*'3'
            s = s1
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 58 and s.count('2') == 23 and s.count('3') == 15:
                print(s1.count('2'), s1)