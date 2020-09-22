sv = []
with open("sv.csv", "rt", encoding="utf-8") as f:
    f.readline() # header
    for line in f:
        s = line.strip().split(",")
        sv.append((int(s[0]), s[1], float(s[2])))
print(max(sv, key=lambda sinh_vien: sinh_vien[2]))
