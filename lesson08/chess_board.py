import turtle as t
import figures

t.hideturtle(); t.tracer(False)
width = 30
for i in range(8):
    for j in range(8):
        color = ("blue" if (i + j) % 2 == 0 else "green")
        figures.square(i*width, j*width, width, color, color)
t.update()
