from fraction import Fraction

nums = []
while text := input("Nhập phân số (Enter để dừng): "):
    nums.append(Fraction(text))
    
nums.sort(reverse=True)
print("Các số đã nhập theo thứ tự giảm dần là:")
print(nums)

k = int(input("Bạn muốn tìm số lớn thứ mấy? "))
if 0 < k <= len(nums):
    print(f"Số lớn thứ {k} đã nhập là {nums[k - 1]}")
