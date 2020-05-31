import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def update(val):
    t = val = int(val)
    if val == 1:
        tex = "y = x"
    elif val > 1:
        tex = "y = $x^{%d}$" % val
    else:
        t = 1/(-val + 2)
        tex = r"y = $x^{\frac{1}{%d}}$" % (-val + 2)
    
    ys = [x**t for x in xs]
    ax.clear()
    ax.plot(xs, ys, color="r")
    ax.set_title(tex)
    
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2)
slider_ax = plt.axes([0.1, 0.1, 0.8, 0.03])
slider = Slider(slider_ax, "val", -14, 15, valinit=1, valstep=1, valfmt='%d')
slider.on_changed(update)
    
xs = [i/1000 for i in range(1001)]
ax.set_ylim(0, 1)
ax.set_xlim(0, 1)
update(1)

plt.show()
