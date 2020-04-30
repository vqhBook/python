while text := input("Nhập số nguyên dương n: "):
    n = int(text)
    num = 0
    print(n, end=" ")
    while n != 1:
        if n % 2 == 0:  # n chẵn
            n = n // 2
        else:           # n lẻ
            n = 3*n + 1
        num += 1
        print(n, end=" ")

    print("\nSố lần lặp là", num)
