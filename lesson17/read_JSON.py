import json

with open("sv.json", "rt") as f:
    sv = json.load(f)
print(max(sv, key=lambda sinh_vien: sinh_vien[2]))
