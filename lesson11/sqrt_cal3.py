import math
from string import ascii_lowercase as alphabet

def cal_sqrt(methods, nums):
    for method, method_name in methods:
        print(f"Tính căn bằng phương pháp {method_name}:")
        for i in range(len(nums)):
            print("%s) Căn của %g là %.9f" %
                  (alphabet[i], nums[i], method(nums[i])))

# danh sách các số cần tính căn
nums = [0.0196, 1.21, 2, 3, 4, 225/256]

# danh sách các phương pháp tính căn (và tên)
methods = [
    (math.sqrt, "math's sqrt"),
    (lambda x: math.pow(x, 0.5), "math's pow"),
    (lambda x: pow(x, 0.5), "built-in pow"),
    (lambda x: x ** 0.5, "exponentiation operator")
    ]

cal_sqrt(methods, nums)
