n = int(input("Nhập số có không quá 3 chữ số: "))
đơn_vị, chục, ngàn = n % 10, (n % 100) // 10, n // 100
tổng = đơn_vị + chục + ngàn
print("Tổng các chữ số là:", tổng)
