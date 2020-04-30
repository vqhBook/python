import turtle as t

def forward(deg):
    t.setheading(deg)
    t.forward(d)

d = 20
t.shape("turtle")
t.speed("slowest")
t.onkey(lambda: forward(180), "Left")
t.onkey(lambda: forward(0), "Right")
t.onkey(lambda: forward(90), "Up")
t.onkey(lambda: forward(270), "Down")
t.onkey(t.bye, "Escape")
t.listen()
t.mainloop()
