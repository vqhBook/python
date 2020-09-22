n = int(input()) # Không có chuỗi thông báo nhập
a = []  # Pascal triangle

for i in range(n):
    a.append([1] * (i + 1))

for i in range(1, n):
    for j in range(1, i):
        a[i][j] = a[i-1][j-1] + a[i-1][j]

w = 1 + len(str(max([max(row) for row in a]))) # độ rộng canh phải
for i in range(n):
    for j in range(i + 1):
        print(f"%{w}d" % a[i][j], end="")
    print()
