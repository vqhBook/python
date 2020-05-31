n = int(input("Nhập số nguyên không âm: "))
tổng = 0

while n > 0:
    tổng += n % 10
    n //= 10

print("Tổng các chữ số là:", tổng)
