import turtle as t
import math
import time
import figures

t.tracer(False)
t.hideturtle()

t.title("Parabol y = kx^2")
figures.coordinate_system(-4, -10, 4, 10)
for k in range(-25, 26):
    figures.para_curve(lambda t: t, lambda t: k/20 * t**2, -4, 4, 50, line_color="red")
t.update()
time.sleep(5)

t.clear()
t.title("Line y = kx")
figures.coordinate_system(-4, -10, 4, 10)
for k in range(-25, 26):
    figures.para_curve(lambda t: t, lambda t: k/5*t, -4, 4, 50, line_color="red")
t.update()
time.sleep(5)

t.clear()
t.title("Ellipse and Circle")
figures.coordinate_system(-25, -25, 25, 25, coord_color=None)
for a in range(26):
    figures.para_curve(lambda t: a*math.cos(math.radians(t)),
                       lambda t: 25*math.sin(math.radians(t)), 0, 360, 50, line_color="red")
for b in range(26):
    figures.para_curve(lambda t: 25*math.cos(math.radians(t)),
                       lambda t: b*math.sin(math.radians(t)), 0, 360, 50, line_color="red")
t.update()

