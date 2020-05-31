import matplotlib.pyplot as plt

labels = ["Giỏi", "Khá", "Trung bình", "Yếu"]
freqs = [5, 30, 10, 5]
clrs = ["seagreen", "darkorange", "darkviolet", "cyan"]

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.bar(labels, freqs, color=clrs)
for i, f in enumerate(freqs):
    ax1.text(i, f+0.2, str(f), horizontalalignment='center')
ax1.set_ylabel("Số lượng")

ax2.pie(freqs, labels=labels, autopct="%.0f%%", colors=clrs)

plt.show()
