#4
def is_prime(n):
    if n == 1:
        return True
    for i in range(2, round(n/2)+1):
        if n % i == 0:
            return False
    return True
