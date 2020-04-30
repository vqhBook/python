def N(x, y):
    return 8*(x**3) - 12*(x**2)*y + 6*x*(y**2) - y**3

print(N(6, -8))
print(N(-8, 6))
print(N(x=6, y=-8))
print(N(y=-8, x=6))
print(N(x=-8, y=6))
print(N(6, y=-8))
# print(N(y=-8, 6)) # SyntaxError
