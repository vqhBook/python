import math
import sqrt

x = float(input("Nhập số cần tính căn: "))
print(f"Căn của {x} theo Newton: {sqrt.Newton_sqrt(x):.9f}")
print(f"Căn của {x} theo math’s sqrt: {math.sqrt(x):.9f}")
