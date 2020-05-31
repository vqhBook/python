from random import random

def parabol_area(N): # N là số điểm gieo mô phỏng
    points = [(random(), random()) for _ in range(N)]
    N_in = sum([y <= x**2 for x, y in points])
    return N_in/N

if __name__ == "__main__": 
    N = int(input("Bạn muốn gieo bao nhiêu điểm: "))
    print(f"Diện tích vùng dưới parabol là {parabol_area(N):.4f}")
