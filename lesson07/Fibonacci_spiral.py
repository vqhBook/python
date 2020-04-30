import turtle as t

x, y = 0, 1
while x <= 377:
    t.circle(x, 90)
    x, y = y, x + y

t.hideturtle()
