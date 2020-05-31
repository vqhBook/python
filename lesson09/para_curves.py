import turtle as t
from math import cos, sin, radians as rad
from figures import para_curve as pcur, coordinate_system

t.setup(600, 600)
t.tracer(False)
coordinate_system(-4, -2, 4, 6)

pcur(lambda t: t, lambda t: t**2, -4, 4, 30,
     line_color="red")
pcur(lambda t: t, lambda t: t + 2, -4, 4, 1,
     line_color="green")
pcur(lambda t: 2*cos(rad(t)), lambda t: 2*sin(rad(t)),
     0, 360, 50, line_color="blue")
pcur(lambda t: 4*cos(rad(t)), lambda t: 2*sin(rad(t)),
     0, 360, 50, line_color="orange")

t.update()
