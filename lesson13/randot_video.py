import random
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.figure import figaspect

def update(_):
    xy_choices = random.choices(xys, weights, k=K)
    for xy in xy_choices:
        out_im.putpixel(xy, (0, 0, 0))

    ax.clear()
    ax.axis("off")
    ax.imshow(out_im)

t = 4.0 # tham số điều khiển mật độ
K = 100 # số điểm trong một lần update  

im = Image.open("image.jpeg").convert("L")
xys = [(x, y) for x in range(im.width) for y in range(im.height)]
weights = [((255 - im.getpixel(xy))/255)**t for xy in xys]
out_im = Image.new("RGB", im.size, color=(255, 255, 255))

FPS = 24
fig, ax = plt.subplots(figsize=figaspect(im.height/im.width))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
matplotlib.rcParams['animation.ffmpeg_path'] = r'D:\ffmpeg\bin\ffmpeg.exe'
ani = FuncAnimation(fig, update, frames=FPS*60)

print("Wait a Minute!")
ani.save("random_dots.mp4", writer=FFMpegWriter(fps=FPS))
print("Done!")
