import math

class SqrtMethod:
    def __init__(self, func, name):
        self.name = name
        try:
            func(1.0)
            self.func = func
        except TypeError:
            raise SqrtMethodError(f"hàm tính căn {name} không hợp lệ!", func)

    def cal_sqrt(self, nums):
        print(f"Tính căn bằng phương pháp {self.name}:")
        for num in nums:
            print(f"Căn của {num} là {self.func(num):.9f}")


class SqrtMethodError(TypeError):
    def __init__(self, msg, func):
        super().__init__(msg)
        self.func = func


try:
    sqrt1 = SqrtMethod(math.sqrt, "math's sqrt")
    sqrt1.cal_sqrt([2, 4])
    sqrt2 = SqrtMethod(math.pow, "math's pow")
    sqrt2.cal_sqrt([2, 4])
except SqrtMethodError as err:
    print(f"Có lỗi tính căn: {err.args[0]}, {err.func}")
