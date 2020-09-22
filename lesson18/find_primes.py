import math

def prime(n): # n là số nguyên > 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: # n có ước > 1 và <= căn n
            return False
    return True

def naive_find_primes(n):
    return [i for i in range(2, n+1) if prime(i)]

def Sieve_of_Eratosthenes(n):
    sieve = [True for _ in range(n + 1)]
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            m = i**2
            while m <= n:
                sieve[m] = False
                m += i
    return [i for i in range(2, n+1) if sieve[i]]

import time
n = 1_000_000
t0 = time.time(); Sieve_of_Eratosthenes(n); print(time.time() - t0)
t0 = time.time(); naive_find_primes(n); print(time.time() - t0)
