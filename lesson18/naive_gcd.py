def naive_gcd(a, b): # a, b > 0
    divisors_a = {d for d in range(1, a+1) if a % d == 0}
    divisors_b = {d for d in range(1, b+1) if b % d == 0}
    common_divisors = divisors_a & divisors_b
    return max(common_divisors)
