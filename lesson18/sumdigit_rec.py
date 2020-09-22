def sum_digits(n):
    if n < 10:
        return n

    return sum_digits(n // 10) + n % 10
