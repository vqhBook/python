import turtle as t
import string

class WriteChar:
    def __init__(self, char):
        self.char = char
        
    def write(self):
        t.clear()
        t.write(self.char, align="center", font=f"Arial {s}")
        t.update()
    

s = 300
t.hideturtle(); t.tracer(False); t.color("red")
t.up(); t.right(90); t.forward(2*s//3); t.down()

for char in string.ascii_letters + string.digits:
    t.onkey(WriteChar(char).write, char)
    
t.listen()
t.exitonclick()
