#1
def number_of_matches(J, S):
    J = set(J)
    k = 0
    for i in J:
        for j in S:
            if i == j:
                k += 1
    return k
number_of_matches('z', 'ZZ')