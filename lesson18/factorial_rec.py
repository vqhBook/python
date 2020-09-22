def fact(n): # n là số nguyên dương
    if n == 1:
        return 1

    return fact(n - 1) * n
