import random
import matplotlib.pyplot as plt

N = 10_000
nums = [random.random() for _ in range(N)]

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(nums, bins=10, rwidth=0.95)
ax2.boxplot(nums)
plt.show()
