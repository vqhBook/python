max1, max2 = None, None
while text := input("Nhập số nguyên (Enter để dừng): "):
    num = int(text)
    if not max1 or max1 < num:
        max2, max1 = max1, num
    elif (num < max1) and (not max2 or max2 < num):
        max2 = num

if max2:
    print("Số lớn thứ hai đã nhập là:", max2)
else:
    print("Không có số lớn thứ hai")
