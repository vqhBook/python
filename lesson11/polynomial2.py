def eval_polynomial(P, x):
    return sum([a * x**k for k, a in enumerate(P)])

# Tính giá trị của đa thức x + 2x^3 - 3x^5 tại x = 2
print(eval_polynomial([0, 1, 0, 2, 0, -3], 2))
