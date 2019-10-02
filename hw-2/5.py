#5
def is_valid(braces_string):
    a = 0
    b = 0
    for i in braces_string:
        if i == "(":
            a += 1
        else:
            b += 1
    if a == b:
        return True
    else:
        return False
print(is_valid("()"))
print(is_valid("("))
print(is_valid("()()"))
print(is_valid("(()("))