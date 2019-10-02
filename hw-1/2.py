#2
#не могу понять как вещественные числа могут быть красивыми, им же всегда False
def get_digit_sum(n):
    s = 0
    for i in str(abs(n)):
        if i == '.':
            continue
        else:
            s+= int(i)
    return s
def is_beauty(n):
    return n % get_digit_sum(n) == 0
