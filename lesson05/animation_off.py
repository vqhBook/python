import turtle as t

x = t.numinput("Hello", "Enter radius: ")
y = 2**0.5 * x
t.hideturtle()
t.color("black", "yellow")

t.tracer(False)
t.up(); t.forward(x); t.left(135); t.down()
t.begin_fill()
t.forward(y); t.left(90); t.forward(y); t.left(90)
t.forward(y); t.left(90); t.forward(y); t.left(90)
t.end_fill()
t.update()
