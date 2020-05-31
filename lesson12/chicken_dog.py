for x, y in [(i, j) for i in range(37) for j in range(37)]:
    if x + y == 36 and 2*x + 4*y == 100:
        print(f"Số gà là: {x}, số chó là: {y}.")
