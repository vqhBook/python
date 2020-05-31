import turtle as t

t.shape("turtle")
d = 20
actions = {"L": 180, "R": 0, "U": 90, "D": 270}
while ins := input("Nhập chuỗi lệnh cho con rùa (L, R, U, D): "):
    for act in ins:
        if act in actions:
            t.setheading(actions[act])
        else:
            continue
        t.forward(d)
print("Done!")
