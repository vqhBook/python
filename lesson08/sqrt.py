"""Module hỗ trợ việc tính căn bằng phương pháp Newton.

Tác giả: Vũ Quốc Hoàng.
Ngày viết: 10-03-2020.
"""

def Newton_sqrt(x):
    """Tính căn theo phương pháp Newton.

    Số cần tính căn, x, phải là số dương.
    """
    y = x
    for i in range(100):
        y = y/2 + x/(2*y)
    return y
