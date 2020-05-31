def eval_polynomial(P, x):
    s = 0
    for k, a in enumerate(P):
        s += a * x**k
    return s

# Tính giá trị của đa thức x + 2x^3 - 3x^5 tại x = 2
P = [0, 1, 0, 2, 0, -3]
print(eval_polynomial(P, 2))
