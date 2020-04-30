import turtle as t

r = 120
t.up()
t.left(90); t.forward(r); t.left(90)
t.down()

t.color("#FF0000")          # Red
t.begin_fill(); t.circle(r, 120); t.end_fill()

t.colormode(255)
t.color((0, 255, 0))        # Green
t.begin_fill(); t.circle(r, 120); t.end_fill()

t.colormode(1.0)
t.color((0.0, 0.0, 1.0))    # Blue
t.begin_fill(); t.circle(r, 120); t.end_fill()

t.hideturtle()
