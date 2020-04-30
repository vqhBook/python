import turtle as t
import time

t.hideturtle(); t.tracer(False)
for i in range(100):
    t.clear()
    t.write(i, align="center", font=("Arial", 150, "normal"))
    t.update()
    time.sleep(1)
