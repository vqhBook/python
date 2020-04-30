def Newton_sqrt(x):
    "Tính căn theo phương pháp Newton."
    y = x
    for i in range(100):
        y = y/2 + x/(2*y)
    return y

print(f"Căn của 2 theo Newton: {Newton_sqrt(2):.9f}")
print(Newton_sqrt.__doc__)
help(Newton_sqrt)
