nums = []
while text := input("Nhập số nguyên (Enter để dừng): "):
    nums.append(int(text))

nums.sort(reverse=True)

k = int(input("Bạn muốn tìm số lớn thứ mấy? "))
if 0 < k <= len(nums):
    print(f"Số lớn thứ {k} đã nhập là {nums[k - 1]}")
