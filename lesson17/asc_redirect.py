import sys
import runpy

stdin = sys.stdin
with open("rand_int.txt", "rt") as f:
    sys.stdin = f
    runpy.run_module("ascending")
sys.stdin = stdin
