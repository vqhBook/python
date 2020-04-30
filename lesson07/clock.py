import turtle as t
import time

t.hideturtle(); t.tracer(False)
while True:
    now = time.localtime()
    time_str = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
    t.clear()
    t.write(time_str, align="center", font=("Arial", 100, "normal"))
    t.update()
    time.sleep(0.1)
