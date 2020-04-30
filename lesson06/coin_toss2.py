import random

coin = random.randint(0, 1)
choice = input("Bạn chọn ngửa hay sấp(N/S)? ")
print("Đồng xu ra " + ("ngửa" if coin == 1 else "sấp"))
print("Bạn chọn " + ("ngửa" if choice == "N" else "sấp"))
if (coin == 1 and choice == "N"
    or coin == 0 and choice == "S"):
    print("Bạn lên voi!")
else:
    print("Bạn xuống chó!")
