def Euclid_gcd2(a, b): # a, b >= 0
    while b > 0:
        a, b = b, a % b
    return a
