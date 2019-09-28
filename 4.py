#4
def is_prime(n):
    if n == 1:
        return True
    d = 2
    while n % d != 0:
        d += 1
        return d == n
