import turtle as t
import math
import time
import figures

t.hideturtle()

t.clear()
t.title("Hyperbolic spiral")
figures.polar_para_curve(lambda t: 300*360/t,
                         lambda t: t, 360, 5*360, 4*50, line_color="red")
t.update()
time.sleep(2)

t.clear()
t.title("Golden spiral")
phi = (1 + math.sqrt(5))/2
figures.polar_para_curve(lambda t: phi**(t/90),
                         lambda t: t, 0, 3*360, 3*50, line_color="red")
t.update()
time.sleep(2)

t.clear()
t.title("Rose 1")
figures.polar_para_curve(lambda t: 200*math.cos((math.pi/180) * (5/2*t)),
                         lambda t: t, 0, 2*360, 200, line_color="red")
t.update()
time.sleep(2)

t.clear()
t.title("Rose 2")
figures.polar_para_curve(lambda t: 200*math.cos((math.pi/180) * (5/6*t)),
                         lambda t: t, 0, 6*360, 6*50, line_color="red")
t.update()
time.sleep(2)

t.clear()
t.title("Rose 3")
figures.polar_para_curve(lambda t: 40 + 200*math.cos((math.pi/180) * (12*t)),
                         lambda t: t, 0, 360, 500, line_color="pink", fill_color="pink")
