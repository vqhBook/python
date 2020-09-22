import sys
import runpy

stdin, stdout = sys.stdin, sys.stdout
with open("rand_int.txt", "rt") as infile, \
     open("sorted_int.txt", "wt") as outfile:
    sys.stdin = infile
    sys.stdout = outfile
    runpy.run_module("ascending")
sys.stdin, sys.stdout = stdin, stdout
