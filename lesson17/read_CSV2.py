import csv

sv = []
with open("sv2.csv", "rt", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    sv = list(reader)
print(max(sv, key=lambda sinh_vien: sinh_vien[2]))
