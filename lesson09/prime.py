import math

def prime1(n): # n là số nguyên > 1
    ndivs = 0 # số lượng ước số dương của n
    for i in range(1, n + 1):
        if n % i == 0: # i là ước của n
            ndivs += 1
    return (ndivs == 2) # n có đúng 2 ước số
	    
def prime2(n): # n là số nguyên > 1
    for i in range(2, n):
        if n % i == 0:
            return False # n có ước > 1 và < n
    return True
	
def prime3(n): # n là số nguyên > 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False # n có ước > 1 và <= căn n
    return True
