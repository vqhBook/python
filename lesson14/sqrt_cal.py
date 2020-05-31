import math

class SqrtMethod:
    """Class for square root methods"""
    
    def __init__(self, func, name):
        self.func = func
        self.name = name

    def cal_sqrt(self, nums):
        print(f"Tính căn bằng phương pháp {self.name}:")
        for num in nums:
            print(f"Căn của {num} là {self.func(num):.9f}")

if __name__ == "__main__":
    sqrt_methods = [
        SqrtMethod(math.sqrt, "math's sqrt"),
        SqrtMethod(lambda x: math.pow(x, 0.5), "math's pow"),
        SqrtMethod(lambda x: pow(x, 0.5), "built-in pow"),
        SqrtMethod(lambda x: x ** 0.5, "exponentiation operator"),
        ]
    nums = [0.0196, 1.21, 2, 3, 4, 225/256]
    for sqrt_method in sqrt_methods:
        sqrt_method.cal_sqrt(nums)
