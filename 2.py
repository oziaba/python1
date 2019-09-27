#2
#только для целых чисел пока
def get_digit_sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return s  
def is_beauty(n):
    return n % get_digit_sum(n) == 0
