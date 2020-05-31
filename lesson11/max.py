max = None
while text := input("Nhập số nguyên (Enter để dừng): "):
    num = int(text)
    if not max or max < num:
        max = num

if max:
    print("Số lớn nhất đã nhập là", max)
