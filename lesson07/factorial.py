n = int(input("Nhập số nguyên dương: "))
f = 1
for i in range(1, n + 1):
    f *= i
print(f"{n}! = {f}")
