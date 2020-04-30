import turtle as t
	
def square(x, y, width, line_color="black", fill_color=None):
    t.up(); t.goto(x, y); t.down()
    t.setheading(0); t.pencolor(line_color)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(width)
        t.left(90)
    if fill_color:
        t.end_fill()
