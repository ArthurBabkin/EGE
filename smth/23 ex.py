def f(x, finish):
    if x > finish: return 0
    if x == finish: return 1
    if x< finish: return f(x+2, finish)+f(x+7, finish)
print(f(5,49))