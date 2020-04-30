import turtle as t
t.hideturtle()

t.color("saddle brown")
t.begin_fill()
t.goto(100, 0); t.goto(100, -200); 
t.goto(-100, -200); t.goto(-100, 0)
t.end_fill()

t.color("orange red")
t.begin_fill()
t.goto(200, 0); t.setheading(90); t.circle(200, 180); t.goto(0, 0)
t.end_fill()
