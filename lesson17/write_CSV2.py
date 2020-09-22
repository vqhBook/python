import csv

sv = [(19001, "SV A", 6.0),
      (19005, "SV B", 7.5),
      (19004, "SV C", 5.0),
      (19010, "SV D", 0.5),
      (19009, "SV E", 10.0)]

sv.sort(key=lambda sinh_vien: sinh_vien[0])
with open("sv2.csv", "wt", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sv)
