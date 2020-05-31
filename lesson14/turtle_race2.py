import turtle as t
from turtle import window_width as ww, window_height as wh
from random import randint as rint, random as rfloat

class PizzaTurtle(t.Turtle):
    all_pizzas = []

    def __init__(self, shape_file, radius=20, value=1):
        super().__init__()
        self.radius = radius; self.value = value
        self.shape(shape_file); self.ondrag(self.goto)
        self.up(); self.goto(random_point(self.radius))

        PizzaTurtle.all_pizzas.append(self)
        
class NinjaTurtle(t.Turtle):
    all_ninjas = []

    def __init__(self, name, color="black", radius=10):
        super().__init__()
        self.name = name; self.radius = radius;
        self.score = 0; self.color(color)
        self.shape("turtle")
        self.setheading(rint(0, 360))
        self.up()
        self.goto(random_point(self.radius))
        self.down()

        NinjaTurtle.all_ninjas.append(self)

    def move(self):
        for other_tur in NinjaTurtle.all_ninjas:
            if (self is not other_tur and
                self.distance(other_tur) < 2*self.radius):
                self.setheading(rint(0, 360))

        if abs(self.xcor()) >= ww()/2 - self.radius:
            self.setheading((180 - self.heading()) % 360)
        if abs(self.ycor()) >= wh()/2 - self.radius:
            self.setheading((360 - self.heading()) % 360)
        self.forward(2)

def random_point(r):
    x = rint(-ww()//2 + r, ww()//2 - r)
    y = rint(-wh()//2 + r, wh()/2 - r)
    return (x, y)

def check_winner():
    for pizza in PizzaTurtle.all_pizzas:
        removed = False
        for tur in NinjaTurtle.all_ninjas:
            if pizza.distance(tur) < pizza.radius/2:
                tur.score += pizza.value
                print(tur.name, "win pizza value", pizza.value)
                print(tur.name, "'s score is", tur.score)
                removed = True
        if removed:
            pizza.hideturtle()
            t.update()
            PizzaTurtle.all_pizzas.remove(pizza)

    if len(PizzaTurtle.all_pizzas) == 0:
        max_score = (max(NinjaTurtle.all_ninjas,
                    key=(lambda tur: tur.score))).score
        for tur in NinjaTurtle.all_ninjas:
            if tur.score == max_score:
                print(tur.name, "win the race!")
                tur.turtlesize(2.5, 2.5)
        print("The winning score is", max_score)
        return True
    return False

def run():
    if check_winner():
        t.update()
        return
    for tur in NinjaTurtle.all_ninjas:
        tur.move()
    t.update(); t.ontimer(run, 10)

t.title("Teenage Mutant Ninja Turtles Race for Pizza!")
t.addshape("pizza.gif"); t.tracer(False)

for i in range(50):
    PizzaTurtle("pizza.gif")
for i in range(100):
    NinjaTurtle(f"#{i+1}", color=(rfloat(), rfloat(), rfloat()))

t.onkeypress(t.bye); t.listen()
run(); t.mainloop()
