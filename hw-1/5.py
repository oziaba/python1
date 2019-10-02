#5
def is_self_dividing(n):
    d = 0
    k = len(str(n))
    for i in str(n):
        if n % int(i) == 0:
            d += 1
    if d == k:
        return True
    else:
        return False
