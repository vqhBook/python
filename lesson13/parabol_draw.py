import matplotlib.pyplot as plt
import matplotlib

fig, ax = plt.subplots()

# Đặt hệ trục đều (đơn vị bằng nhau cho 2 trục)
ax.axis("equal")

# Không hiển thị hệ trục
ax.axis("off")

# Vẽ và tô hình vuông đơn vị
ax.fill([0, 0, 1, 1], [0, 1, 1, 0], facecolor='bisque', edgecolor='black', linewidth=0.5)

# Vẽ đoạn thẳng chéo (0, 0) đến (1, 1)
xs = [i/100 for i in range(101)]
ax.plot(xs, xs, color="red")

# Vẽ parabol y = x^2 trong khoảng [0, 1]
ys = [x**2 for x in xs]
ax.plot(xs, ys, color="blue")

# Tô vùng bên dưới parabol
ax.fill(xs + [1, 0], ys + [0, 0], facecolor='cornflowerblue', edgecolor='black', linewidth=0.5)

# Vẽ 3 điểm minh họa cùng với các đường gióng
x0 = 0.75
psx, psy = [x0]*3, [0.4, 0.75**2, 0.9]
ax.plot(psx, psy, "o", color="black")
ax.plot([x0, x0], [0, max(psy)], ":", color="black", linewidth=0.5)
for x, y in zip(psx, psy):
    ax.plot([0, x], [y, y], ":", color="black", linewidth=0.5)

# Đặt font mặc định là serif với size là 11 pt
matplotlib.rcParams["font.size"] = 11
matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["mathtext.fontset"] = "cm"

# Xuất các điểm tọa độ (dùng Latex để hiển thị công thức Toán)
ax.text(-0.06, -0.06, "0")
ax.text(1, -0.06, "1")
ax.text(-0.06, 1, "1")
ax.text(x0, -0.06, "$x_0$")
for index, y in enumerate(psy):
    ax.text(-0.06, y, r"$y_{%d}$" % (index + 1))
    ax.text(x0 + 0.02, y, r"$P_{%d}$" % (index + 1))

# Chú thích các đường (dùng Latex để hiển thị công thức Toán)
ax.annotate("$y = x$", xy=(0.5, 0.5), xytext=(0.25, 0.65),
            arrowprops=dict(facecolor='black', width=0.5, headwidth=5, shrink=0.05))
ax.annotate("$y = x^2$", xy=(0.5, 0.25), xytext=(0.2, 0.48),
            arrowprops=dict(facecolor='black', width=0.5, headwidth=5, shrink=0.05))

plt.show()
