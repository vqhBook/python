from PIL import Image

im = Image.open("image.jpeg")
red, _, blue = im.split()
green = Image.new("L", im.size, 0)
out_im = Image.merge("RGB", (red, green, blue))
out_im.save("image_violet.jpeg")
out_im.show()
