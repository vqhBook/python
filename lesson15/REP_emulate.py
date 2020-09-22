from math import *

while True:
    exp = input(">>> ")
    if exp == "quit()":
        break
    if exp.strip() == "":
        continue
    
    try:
        val = eval(exp)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    else:
        if val != None:
            print(val)
