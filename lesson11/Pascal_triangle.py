n = int(input("Nhập số dòng n: "))
a = []  # Pascal triangle

for i in range(n):
    a.append([1] * (i + 1))

for i in range(1, n):
    for j in range(1, i):
        a[i][j] = a[i-1][j-1] + a[i-1][j]

for i in range(n):
    for j in range(i + 1):
        print("%5d" % a[i][j], end="")
    print()
