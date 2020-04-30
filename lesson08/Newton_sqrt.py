import math

def Newton_sqrt(x):
    y = x
    for i in range(100):
        y = y/2 + x/(2*y)
    return y

print(f"Căn của 2 theo Newton: {Newton_sqrt(2):.9f}")
print(f"Căn của 2 theo math’s sqrt: {math.sqrt(2):.9f}")

x = float(input("Nhập số cần tính căn: "))
print(f"Căn của {x} theo Newton: {Newton_sqrt(x):.9f}")
print(f"Căn của {x} theo math’s sqrt: {math.sqrt(x):.9f}")
