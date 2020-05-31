from PIL import Image, ImageDraw

size = (250, 250)
im = Image.new("RGB", size, "red")
d = ImageDraw.Draw(im)
d.ellipse([(0, 0), size], fill="blue")
im.save("pillow_draw.png")
im.show()
