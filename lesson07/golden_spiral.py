import turtle as t
t.speed("slowest")

phi = (1 + 5**0.5)/2
r = 377
t.left(90)
for i in range(12):
    t.circle(-r / phi**i, 90)

t.hideturtle()
