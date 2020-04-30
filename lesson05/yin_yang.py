import turtle as t
r = 120

t.color("red")
t.begin_fill(); t.circle(r); t.end_fill()

t.color("black")
t.begin_fill()
t.circle(r, 180); t.circle(r/2, 180); t.circle(-r/2, 180)
t.end_fill()

t.right(90); t.up(); t.forward(r/2 - r/10); t.right(90)
t.color("black")
t.begin_fill(); t.circle(r/10); t.end_fill()

t.left(90); t.up(); t.forward(r); t.right(90)
t.color("red")
t.begin_fill(); t.circle(r/10); t.end_fill()

t.hideturtle()
