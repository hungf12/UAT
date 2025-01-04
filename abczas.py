def f(x, y=[]):
    y.append(x)
    return y, id(y)

print(f(23))
print(f(42))