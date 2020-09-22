def Euclid_gcd(a, b): # a, b >= 0
    if b == 0:
        return a
    return Euclid_gcd(b, a % b)
