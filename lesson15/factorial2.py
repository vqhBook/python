import math

while True:
    try:
        n = int(input("Nhập n: "))
        break
    except ValueError:
        print(f"Giá trị nhập không hợp lệ!")

print(f"Giai thừa của {n} là {math.factorial(n)}")
