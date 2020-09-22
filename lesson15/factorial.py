import math

try:
    n = int(input("Nhập n: "))
except ValueError:
    n = 1
    print(f"Giá trị nhập không hợp lệ! n nhận giá trị mặc định là {n}.")

print(f"Giai thừa của {n} là {math.factorial(n)}")
