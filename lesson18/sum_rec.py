def S(n): # n là số nguyên không âm
    if n == 0:
        return 0

    return S(n - 1) + n
