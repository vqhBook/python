n = int(input("Nhập số có không quá 3 chữ số: "))
tổng = 0

for _ in range(3):
    tổng += n % 10
    n //= 10

print("Tổng các chữ số là:", tổng)
