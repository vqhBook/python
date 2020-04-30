char = input("Nhập kí hiệu vẽ: ")
n = int(input("Nhập chiều cao: "))
for i in range(1, n + 1):
    for _ in range(i):
        print("*", end="")
    print() # xuống dòng
