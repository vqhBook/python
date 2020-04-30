n = int(input("Nhập số nguyên dương: "))
f, i = 1, 1
while i <= n:
    f *= i
    i += 1
print(f"{n}! = {f}")
