import sys
import runpy

stdout = sys.stdout
with open("Pascal_triangle.txt", "wt") as f:
    sys.stdout = f
    runpy.run_module("Pascal_triangle")
sys.stdout = stdout
