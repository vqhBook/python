import turtle as t

def forward(deg):
    def _forward():
        t.setheading(deg)
        t.forward(d)
        
    return _forward
    
t.shape("turtle")
d = 20
actions = {"Left": 180, "Right": 0, "Up": 90, "Down": 270}
for act in actions:
    t.onkey(forward(actions[act]), act)
t.onkey(t.bye, "Escape")
t.listen()
t.mainloop()
