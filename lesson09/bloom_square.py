import turtle as t
import time
import figures

def toggle_bloom():
    global bloom
    bloom = not bloom

def run():
    global bloom, width

    max_width = min(t.window_width(), t.window_height())
    if width <= 0 and not bloom: bloom = True
    if width >= max_width and bloom: bloom = False
    width += (1 if bloom else -1)
    
    t.clear()
    figures.square(-width//2, -width//2, width, "red", "red")
    t.update()
    t.ontimer(run, 1000//24) # 24 fps

width = 0; bloom = True
t.hideturtle(); t.tracer(False)
t.onkey(toggle_bloom, "space"); t.listen()
run(); t.exitonclick()
