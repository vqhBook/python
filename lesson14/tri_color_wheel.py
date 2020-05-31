import turtle as t
import time
import math

class TriColorWheel:
    def __init__(self, omega, center=(0, 0), radius=100,
                 colors=("red", "green", "blue"),
                 up_key=None, down_key=None):
        self.center = center
        self.radius = radius
        self.colors = colors
        self.omega = omega  # vận tốc góc độ/giây (+, 0, -)
        self.angle = 0      # góc điểm chốt A
        if up_key: t.onkeypress(self.speed_up, up_key)
        if down_key: t.onkeypress(self.speed_down, down_key)

    def speed_up(self): self.omega += 2

    def speed_down(self): self.omega -= 2

    def rotate(self, dt):
        self.angle += self.omega * dt
        A = self.angle; B = A + 120; C = B + 120
        t.up(); t.goto(self.center); t.down()
        for angle, color in zip((A, B, C), self.colors):
            t.color(color)
            t.begin_fill()
            t.setheading(angle); t.forward(self.radius); t.left(90)
            t.circle(self.radius, 120); t.goto(self.center)
            t.end_fill()

    def contain(self, point):
        return math.dist(point, self.center) <= self.radius

if __name__ == "__main__":
    def run():
        global tm
        
        t.clear()
        tcw1.rotate(time.time() - tm)
        tcw2.rotate(time.time() - tm)
        t.update()
        tm = time.time()
        t.ontimer(run, 1000//24) # 24 fps

    tcw1 = TriColorWheel(180, center=(100, 0),
                         up_key="Left", down_key="Right")
    tcw2 = TriColorWheel(-180, center=(-100, 0),
                    colors=("cyan", "magenta", "yellow"),
                    up_key="a", down_key="d")

    t.tracer(False); t.hideturtle(); t.listen()
    tm = time.time(); run(); t.exitonclick()
