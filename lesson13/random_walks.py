import random
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def neighbours(p):
    x, y = xys[p]
    neigs = [(x + i, y + j) for i in range(-R, R + 1) for j in range(-R, R + 1)
             if 0 <= x + i < im.width and 0 <= y + j < im.height]
    weigs = [weights[i*im.height + j] for i, j in neigs]
    return neigs, weigs

def update(_):
    for _ in range(K):
        for i, p in enumerate(walks):
            [(x, y)] = random.choices(*neighbours(p))
            lengths[i] -= 1
            if lengths[i] < 0:
                [walks[i]] = random.choices(range(len(xys)), weights)
                lengths[i] = L
            else:
                out_draw.line([xys[p], (x, y)], fill="black", width=1)
                walks[i] = x*im.height + y

    ax.clear()
    ax.imshow(out_im)

t = 4.0     # tham số điều khiển mật độ
K = 50      # số lần đi trong một lần update
N = 10      # số walk
R = 6       # kích thước lân cận
L = 200     # chiều dài tối đa của walk

im = Image.open("image.jpeg").convert("L")
xys = [(x, y) for x in range(im.width) for y in range(im.height)]
weights = [((255 - im.getpixel(xy))/255)**t for xy in xys]
out_im = Image.new("RGB", im.size, color=(255, 255, 255))
out_draw = ImageDraw.Draw(out_im)
walks = random.choices(range(len(xys)), weights, k=N)
lengths = [L for _ in range(N)]

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000//24)
plt.show()

out_im.save("image_walk.png")
