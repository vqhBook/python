import turtle as t
import time
from random import randint, random
from tri_color_wheel import TriColorWheel

def on_click(x, y):
    for i in range(len(tcws)):
        if tcws[i].contain((x, y)):
            tcws[i], tcws[-1] = tcws[-1], tcws[i]
            return

def run():
    global tm
    
    t.clear()
    for tcw in tcws:
        tcw.rotate(time.time() - tm)
    t.update()
    tm = time.time()
    t.ontimer(run, 1000//24) # 24 fps

W, H = 600, 600
tcws = []
for _ in range(25):
    radius = randint(10, H//4)
    center = (randint(-W//2, W//2), randint(-H//2, H//2))
    omega = randint(0, 360*2)
    colors = tuple((random(), random(), random())
                   for _ in range(3))
    tcws.append(TriColorWheel(omega, center, radius, colors))

t.setup(W, H); t.tracer(False); t.hideturtle()
t.onscreenclick(on_click)
t.onkeypress(lambda: tcws[-1].speed_up(), "Left")
t.onkeypress(lambda: tcws[-1].speed_down(), "Right")
t.onkeypress(t.bye, "Escape")
t.listen(); tm = time.time()
run(); t.mainloop()
