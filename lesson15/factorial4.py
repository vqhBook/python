import math
import warnings

n = int(input("Nhập n: "))

if n >= 0:
    f = math.factorial(n)
else: # n < 0
    warnings.warn("n nên không âm!", UserWarning)
    f = -math.factorial(-n)
    
print(f"Giai thừa của {n} là {f}")
