import turtle as t

def rotate(deg):
    t.setheading(deg)

def forward(level):
    def _forward():
        t.forward(level * d)
    return _forward

d = 5
t.shape("turtle")
t.onkey(lambda: rotate(180), "Left")
t.onkey(lambda: rotate(0), "Right")
t.onkey(lambda: rotate(90), "Up")
t.onkey(lambda: rotate(270), "Down")
t.onkey(t.bye, "Escape")

keys = "123456789"
for i in range(len(keys)):
    t.onkey(forward(int(keys[i])), keys[i])

t.listen()
t.mainloop()
