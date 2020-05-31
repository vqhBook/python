import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame):
    global N, freqs

    N += 1
    freqs[random.randint(0, 1)] += 1
    fr = [f/N for f in freqs]
    
    ax.clear()
    ax.set_ylim(0, 1)
    ax.bar(["Sấp", "Ngửa"], fr, color=["red", "blue"])
    ax.text(0, fr[0] + 0.01, f"{fr[0]*100:.2f}%",
            horizontalalignment='center')
    ax.text(1, fr[1]+ 0.01, f"{fr[1]*100:.2f}%",
            horizontalalignment='center')
    ax.set_title(f"Lần tung thứ {N}")

N = 0
freqs = [0, 0] # Số lượng sấp, ngửa

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000//24)
plt.show()
