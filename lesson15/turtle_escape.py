import turtle as t
import random

t.shape("turtle")
d = 20

try:
    while (abs(t.xcor()) < t.window_width()/2
           and abs(t.ycor()) < t.window_height()/2):
        direction = random.choice("LRUD")
        if direction == "L":
            t.setheading(180)
        elif direction == "R":
            t.setheading(0)
        elif direction == "U":
            t.setheading(90)
        else: # direction == "D"
            t.setheading(270)
        t.forward(d)
    print("Congratulations!")

except t.Terminator:
    pass
