def Newton_sqrt(x):
    if x < 0:
        raise ValueError("math domain error")
    if x == 0:
        return 0.0

    y = x
    for i in range(100):
        y = y/2 + x/(2*y)
    return y
