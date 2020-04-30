import turtle as t
t.speed("slowest")

PHI = (1 + 5**0.5)/2
r = 377

t.left(90)
t.circle(-r, 90); t.circle(-r/PHI, 90)
t.circle(-r/PHI**2, 90); t.circle(-r/PHI**3, 90)
t.circle(-r/PHI**4, 90); t.circle(-r/PHI**5, 90)
t.circle(-r/PHI**6, 90); t.circle(-r/PHI**7, 90)
t.circle(-r/PHI**8, 90); t.circle(-r/PHI**9, 90)
t.circle(-r/PHI**10, 90); t.circle(-r/PHI**11, 90)

t.hideturtle()
