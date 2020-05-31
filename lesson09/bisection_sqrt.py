import math

def bisec_sqrt(x): # x > 0
    l, r = 0, max(x, 1)
    y = (l + r)/2
    while not math.isclose(y*y, x):
        if y*y > x:
            r = y
        else:
            l = y
        y = (l + r)/2
    return y

def Newton_sqrt(x): # x > 0
    y = x/2
    while not math.isclose(y*y, x):
        y = y/2 + x/(2*y)
    return y
