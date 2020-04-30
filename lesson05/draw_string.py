import turtle as t
t.hideturtle()

t.up(); t.dot(5); t.write("Python 1")
t.goto(100, 0); t.color("red"); t.dot(5)
t.write("Python 2", align="center")
t.goto(50, 100); t.color("blue"); t.dot(15)
t.write("Python 3", align="right", font=("Arial", 30, "italic"))
