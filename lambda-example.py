func = lambda a, b, c: a ** 2 + b ** 2 == c ** 2

print(func(3, 4, 5))
print(func(2, 3, 5))

def faktorial(f):
    if f == 0 or f == 1:
        return 1
    return faktorial(f-1) * f

print(faktorial(3))


