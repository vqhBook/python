import sys
import random

n = int(input("Số lượng số: "))

stdout = sys.stdout
with open("rand_int.txt", "wt") as f:
    sys.stdout = f
    for i in range(n):
        print(random.randint(0, 1_000_000))
sys.stdout = stdout
