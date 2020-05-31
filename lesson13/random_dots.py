import random
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(_):
    xy_choices = random.choices(xys, weights, k=K)
    for xy in xy_choices:
        out_im.putpixel(xy, (0, 0, 0))

    ax.clear()
    ax.imshow(out_im)

t = 4.0 # tham số điều khiển mật độ
K = 200 # số điểm trong một lần update

im = Image.open("image.jpeg").convert("L")
xys = [(x, y) for x in range(im.width) for y in range(im.height)]
weights = [((255 - im.getpixel(xy))/255)**t for xy in xys]
out_im = Image.new("RGB", im.size, color=(255, 255, 255))

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000//24)
plt.show()

out_im.save("image_dot.png")
