import random

coin = random.randint(0, 1)
choice = input("Bạn chọn ngửa hay sấp(N/S)? ")
if coin == 1:
    print("Đồng xu ra ngửa")
    if choice == "N":
        print("Bạn chọn ngửa")
        print("Bạn lên voi!")
    else:
        print("Bạn chọn sấp")
        print("Bạn xuống chó!")
else: # coin là 0
    print("Đồng xu ra sấp")
    if choice == "N":
        print("Bạn chọn ngửa")
        print("Bạn xuống chó!")
    else:
        print("Bạn chọn sấp")
        print("Bạn lên voi!")
