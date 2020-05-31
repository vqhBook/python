from math import factorial, radians, cos

def mycos1(x, n=20):
    s = 0
    for i in range(0, n + 1):
        s += (-1)**i * x**(2*i)/factorial(2*i)
    return s

def mycos2(x, n=20):
    s = 0
    for i in range(0, n + 1):
        mu_2i, gt_2i = 1.0, 1.0 # tính x^(2i) và (2i)!
        for j in range(1, 2*i + 1):
            mu_2i *= x
            gt_2i *= j
        s += (1 if i%2 == 0 else -1) * mu_2i/gt_2i
    return s

def mycos3(x, n=20):
    s = term = 1.0 # tính (-1)^i * x^(2i)/(2i)!
    for i in range(1, n + 1):
        term *= -1 * x*x / ((2*i-1)*(2*i))
        s += term
    return s
