import turtle as t
import random

t.shape("turtle")
d = 20
actions = {"L": 180, "R": 0, "U": 90, "D": 270}
while (abs(t.xcor()) < t.window_width()/2 and
       abs(t.ycor()) < t.window_height()/2):
    direction = random.choice("LRUD")
    t.setheading(actions[direction])
    t.forward(d)
print("Congratulations!")
