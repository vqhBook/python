n = int(input("Nhập số có không quá 3 chữ số: "))
tổng = 0

tổng += n % 10; n //= 10
tổng += n % 10; n //= 10
tổng += n % 10; n //= 10

print("Tổng các chữ số là:", tổng)
