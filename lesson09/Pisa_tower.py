import turtle as t
import time
import figures as fg

def log():
    print(f"Hit(s): {hit}, Time: {time.time() - st:.2f}s, "
          f"Speed: {abs(v):.2f}m/s, Height: {h:.2f}m.")
    
def render():
    t.clear()
    fg.line(0, 0, 3, 0); fg.line(1, 0, 1, HEIGHT)
    fg.string(1, h, f"{h:.1f}", align="right", font_size=12)
    fg.line(1, h, 2, h, "blue"); fg.dot(2, h, 10, "red")
    fg.string(2, h, str(hit), color="green", align="center", font_size=20)
    t.update()

def run():
    global v, h, hit, t0, v0, h0
    
    tm = time.time() - t0
    v, h = v0 - G*tm, h0 + v0*tm - (G/2)*(tm**2)
    if h < 0:
        h = 0; hit += 1; t0 = time.time()
        v0, h0 = K * (VMAX if hit == 1 else v0), 0
        if v0 == 0:
            v, h = 0, 0
            render()
            return
    
    render()
    t.ontimer(run, 1000//24)

HEIGHT = 55.86; G =  9.8; VMAX = (2*G*HEIGHT)**0.5; K = 0.9
st = time.time(); hit = 0
t0, v0, h0 = st, 0, HEIGHT

fg.coordinate_system(0, -HEIGHT/10, 3, HEIGHT*11/10, None)
t.hideturtle(); t.tracer(False)
t.onkey(log, "space"); t.listen()
run(); t.exitonclick()
