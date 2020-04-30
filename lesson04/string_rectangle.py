char = input("Nhập kí hiệu vẽ: ")
ncol = int(input("Nhập số cột: "))
nrow = int(input("Nhập số dòng: "))
line = char * ncol + "\n"
rect = line * nrow 
print("\n" + rect)
