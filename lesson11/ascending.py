nums = []
while text := input("Nhập số nguyên (Enter để dừng): "):
    nums.append(int(text))

if len(nums) > 0:
    print("Các số đã nhập theo thứ tự tăng dần là:")
    for num in sorted(nums):
        print(num, end=" ")
