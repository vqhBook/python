import turtle as t
import random
import figures

t.hideturtle(); t.speed("fastest"); t.colormode(1.0)
for _ in range(100):
    w_width = t.window_width()
    w_height = t.window_height()
    x = random.randint(-w_width//2, w_width//2)
    y = random.randint(-w_height//2, w_height//2)
    width = min(random.randint(0, w_width//2 - x),
                random.randint(0, w_height//2 - y))
    figures.square(x, y, width,
        (random.random(), random.random(), random.random()))
