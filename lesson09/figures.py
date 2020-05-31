import turtle as t
from math import ceil, floor, cos, sin, radians
	
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

def para_curve(f, g, tS, tE, n, line_color="black", fill_color=None):
    t.pencolor(line_color)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    
    d = (tE - tS)/n
    for i in range(n + 1):
        ti = tS + i*d
        x, y = f(ti), g(ti)
        if i == 0:
            t.up()
        else:
            t.down()
        t.goto(x, y)

    if fill_color:
        t.end_fill()

def coordinate_system(minx, miny, maxx, maxy, coord_color="gray"):
    t.setworldcoordinates(minx - 0.4, miny - 0.4, maxx + 0.4, maxy + 0.4)
    t.hideturtle()

    if coord_color:
        t.pencolor(coord_color)
        
        t.up(); t.goto(minx - 0.2, 0); t.down(); t.goto(maxx + 0.2, 0)
        t.up(); t.goto(0, miny - 0.2); t.down(); t.goto(0, maxy + 0.2)

        t.up()
        for i in range(ceil(minx), floor(maxx) + 1):
            t.goto(i, 0); t.dot(3)
            if i != 0:
                t.write(i, align="right", font=("Arial", 10, "normal"))
        for i in range(ceil(miny), floor(maxy) + 1):
            t.goto(0, i); t.dot(3)
            t.write(i, align="right",font=("Arial", 10, "normal"))

def line(x1, y1, x2, y2, line_color="black"):
    t.pencolor(line_color)
    t.up(); t.goto(x1, y1)
    t.down(); t.goto(x2, y2)

def string(x, y, text, color="black", align="left",
           font_name="Arial", font_size=8, font_style="normal"):
    t.up(); t.goto(x, y)
    t.pencolor(color)
    t.write(text, align=align, font=(font_name, font_size, font_style))

def dot(x, y, size=2, color="black"):
    t.up(); t.goto(x, y)
    t.dot(size, color)

def polar_para_curve(f, g, tS, tE, n, line_color="black", fill_color=None):
    t.pencolor(line_color)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    
    d = (tE - tS)/n
    for i in range(n + 1):
        ti = tS + i*d
        r, phi = f(ti), g(ti)
        x, y = r*cos(radians(phi)), r*sin(radians(phi))
        if i == 0:
            t.up()
        else:
            t.down()
        t.goto(x, y)

    if fill_color:
        t.end_fill()
