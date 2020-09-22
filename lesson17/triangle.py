import sys

char = input("Nhập kí hiệu vẽ: ")
n = int(input("Nhập chiều cao: "))

stdout = sys.stdout
with open("triangle.txt", "wt") as f:
    sys.stdout = f
    for i in range(1, n + 1):
        print(char * i)
sys.stdout = stdout
print("Done!")
