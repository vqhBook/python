from random import choice
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def Monty_Hall(doors={"#1", "#2", "#3"}):
    car_door = choice(list(doors))
    choice_door = choice(list(doors))
    open_door = choice(list(doors - {choice_door, car_door}))
    op_door = choice(list(doors - {choice_door, open_door}))
    
    return car_door == choice_door, car_door == op_door

def update(_):
    global N, freqs

    N += K
    results = [Monty_Hall() for _ in range(K)]
    freqs[0] += sum([v for v, _ in results])
    freqs[1] += sum([v for _, v in results])
    fr = [f/N for f in freqs]
    
    ax.clear()
    ax.set_ylim(0, 1)
    ax.bar(["Giữ", "Đổi"], fr, color=["red", "blue"])
    ax.text(0, fr[0], f"{fr[0]*100:.2f}%",
            horizontalalignment='center')
    ax.text(1, fr[1], f"{fr[1]*100:.2f}%",
            horizontalalignment='center')
    ax.set_title(f"Lần chơi thứ {N}")

K = 1000 # số lần chơi mỗi lần update
N = 0
freqs = [0, 0] # Số lượng thắng khi Giữ, Đổi

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000//24) 
plt.show()
