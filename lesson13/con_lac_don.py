from math import pi as PI, sin, cos, sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame):
    t = frame/FPS
    anpha = A0*cos(OMEGA*t - PI)
    x, y = L*sin(anpha), L*(1 - cos(anpha))

    ax.clear()
    ax.axis("equal"); ax.axis("off")
    ax.set_xlim([-1.1*L*sin(A0), 1.1*L*sin(A0)])
    ax.set_ylim([-0.1*L, 1.1*L])
    ax.plot([0, x], [L, y], color="black", linewidth=1)
    ax.plot([x], [y], "o", color="red", markersize=10)

L = 1                   # chiều dài dây treo (m)
OMEGA = sqrt(9.81/L)    # tần số góc (1/s^2)
T = 2*PI/OMEGA          # chu kì dao động (s)
A0 = PI/15              # biên độ góc (rad)
FPS = 24                # frames per second

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000//FPS, frames=round(T*FPS))
ani.save("con_lac_don.gif", writer="pillow")
print("Done!")
