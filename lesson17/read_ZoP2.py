f = open("Zen_of_Python.txt", "rt")
aphorisms = [line.strip() for line in f.readlines()]
f.close()

print(f"Có {len(aphorisms)} khẩu quyết")
while key := input("Bạn muốn đọc khẩu quyết nào? "):
    try:
        # key là số nguyên, tra khẩu quyết thứ key (tính từ 1)
        index = int(key) - 1
        if 0 <= index < len(aphorisms):
            print("#%d: %s" % (index + 1, aphorisms[index]))
    except ValueError:
        # tra khẩu quyết chứa key
        for i, aphorism in enumerate(aphorisms, 1):
            if key in aphorism:
                print("#%d: %s" % (i, aphorism))
