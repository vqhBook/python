import turtle as t

t.shape("turtle")
t.speed("slowest")
d = 20
while ins := input("Nhập chuỗi lệnh (L, R, U, D): "):
    for i in range(len(ins)):
        if ins[i] == "L":
            t.setheading(180)
        elif ins[i] == "R":
            t.setheading(0)
        elif ins[i] == "U":
            t.setheading(90)
        elif ins[i] == "D":
            t.setheading(270)
        else:
            continue
        t.forward(d)
print("Done!")
