import turtle as t
import string

def write(char):
    def _write():
        t.clear()
        t.write(char, align="center", font=f"Arial {s}")
        t.update()
    return _write

s = 300
t.hideturtle(); t.tracer(False); t.color("red")
t.up(); t.right(90); t.forward(2*s//3); t.down()

chars = string.ascii_letters + string.digits
for i in range(len(chars)):
    t.onkey(write(chars[i]), chars[i])
    
t.listen()
t.exitonclick()
