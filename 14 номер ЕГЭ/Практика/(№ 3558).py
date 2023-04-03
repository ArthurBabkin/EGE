for i in range(2, 10):
    x = 1*(i+1)**0 + 0*(i+1)**1 + 1*(i+1)**2
    y = 1*i**0 + 0*i**1 + 1*i**2
    if x-y == 13:
        print(i)