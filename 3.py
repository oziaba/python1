#3
def is_power_of_two(n):
    if n == 0:
        return False
    while n > 1:
        if n % 2 == 1:
            return False
        else:
            n = n // 2
            if n == 1:
                return True
