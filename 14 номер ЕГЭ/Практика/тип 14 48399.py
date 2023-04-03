for x in '0123456789ABCDEF':
    res = int('3D4' + x, 16) + int('4' + x + 'C4', 14)
    if res%154==0:
        print(res//154)