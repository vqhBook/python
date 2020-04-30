import math

def builtin_pow_sqrt(x):
    return pow(x, 0.5)

def math_pow_sqrt(x):
    return math.pow(x, 0.5)

def exp_operator_sqrt(x):
    return x ** 0.5

def Newton_sqrt(x):
    y = x
    for i in range(100):
        y = y/2 + x/(2*y)
    return y

def cal_sqrt(method, method_name):
    print(f"Tính căn bằng phương pháp {method_name}:")
    print(f"a) Căn của 0.0196 là {method(0.0196):.9f}")
    print(f"b) Căn của 1.21 là {method(1.21):.9f}")
    print(f"c) Căn của 2 là {method(2):.9f}")
    print(f"d) Căn của 3 là {method(3):.9f}")
    print(f"e) Căn của 4 là {method(4):.9f}")
    print(f"f) Căn của {225/256} là {method(225/256):.9f}")

cal_sqrt(math.sqrt, "math’s sqrt")
cal_sqrt(builtin_pow_sqrt, "built-in pow")
cal_sqrt(math_pow_sqrt, "math’s pow")
cal_sqrt(exp_operator_sqrt, "exponentiation operator")
cal_sqrt(Newton_sqrt, "Newton’s sqrt")
