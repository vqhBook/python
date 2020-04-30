import turtle as t
t.shape("turtle")

d = 200

t.forward(d); t.left(120)       # 1 --> 2
t.forward(d); t.left(120)       # 2 --> 3
t.forward(d); t.left(120)       # 3 --> 4 (1)

t.up()
t.forward(d/3); t.right(60)     # 1 --> 5 (up)
t.forward(d/3); t.left(120)     # 5 --> 6 (up)
t.down()

t.forward(d); t.left(120)       # 6 --> 7
t.forward(d); t.left(120)       # 7 --> 8
t.forward(d); t.left(120)       # 8 --> 9 (6)
