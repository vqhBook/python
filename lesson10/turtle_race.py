import turtle as t
from turtle import window_width as ww, window_height as wh
from random import randint as rint

def random_point(r):
    x = rint(-ww()//2 + r, ww()//2 - r)
    y = rint(-wh()//2 + r, wh()/2 - r)
    return (x, y)
        
def check_winner():
    for tur in FOUR_TURTLES:
        if Pizza.distance(tur) < Pizza.radius/2:
            print(tur.name + " win the race!")
            tur.turtlesize(2.5, 2.5)
            return True
    return False

def forward_and_reflex():
    for tur in FOUR_TURTLES:
        if abs(tur.xcor()) >= ww()/2 - tur.radius:
            tur.setheading((180 - tur.heading()) % 360)
        if abs(tur.ycor()) >= wh()/2 - tur.radius:
            tur.setheading((360 - tur.heading()) % 360)
        tur.forward(2)

def check_collision():
    for tur in FOUR_TURTLES:
        for other_tur in FOUR_TURTLES:
            if (tur is not other_tur and
                tur.distance(other_tur) < 2*tur.radius):
                tur.setheading(rint(0, 360))

def run():
    if check_winner():
        t.update()
        return
    forward_and_reflex(); check_collision()
    t.update(); t.ontimer(run, 10)

t.title("Teenage Mutant Ninja Turtles Race for Pizza!")
t.addshape("pizza.gif"); t.tracer(False)

Pizza = t.Turtle()
Pizza.shape("pizza.gif"); Pizza.radius = 20
Pizza.up(); Pizza.goto(random_point(Pizza.radius))
Pizza.ondrag(Pizza.goto)

Leo, Mike, Don, Raph = t.Turtle(), t.Turtle(), t.Turtle(), t.Turtle()
for tur, name, color in [(Leo, "Leonardo", "blue"),
                         (Mike, "Michelangelo", "orange"),
                         (Don, "Donatello", "purple"),
                         (Raph, "Raphael", "red")]:
    tur.shape("turtle"); tur.radius = 10
    tur.name = name; tur.color(color, color)
    tur.setheading(rint(0, 360))
    tur.up(); tur.goto(random_point(tur.radius)); tur.down()
FOUR_TURTLES = [Leo, Mike, Don, Raph]
t.onkeypress(t.bye); t.listen()
run(); t.mainloop()
