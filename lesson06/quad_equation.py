print("Chương trình giải phương trình bậc 2: ax^2 + bx + c = 0 (a \u2260 0).")
a = float(input("Nhập hệ số a (a \u2260 0): "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if (delta := b**2 - 4*a*c) > 0:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print("Phương trình có 2 nghiệm phân biệt:")
    print(f"x1 = {x1:.2f}, x2 = {x2:.2f}.")
elif delta < 0:
    print("Phương trình vô nghiệm.")
else:   # delta == 0
    x = -b/(2*a)
    print("Phương trình có nghiệm kép:")
    print(f"x1 = x2 = {x:.2f}.")
