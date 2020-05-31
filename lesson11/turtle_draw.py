import turtle as t

def rotate(deg):
    def _rotate():
        t.setheading(deg)
    return _rotate

def forward(level):
    def _forward():
        t.forward(level * d)
    return _forward

d = 5
t.shape("turtle")

for key, deg in zip(["Left", "Right", "Up", "Down"],
                    [180, 0, 90, 270]):
    t.onkey(rotate(deg), key)

for key in [str(i) for i in range(1, 10)]:
    t.onkey(forward(int(key)), key)

t.onkey(t.bye, "Escape")
t.listen()
t.mainloop()
