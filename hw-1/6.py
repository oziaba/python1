#6
L = [8, 5, 3, 5, 6]
def get_largest_perimiter(L):
    p = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            for k in range(j+1,len(L)):
                if (L[i] + L[j] > L[k]) and (L[i] + L[k] > L[j]) and (L[k] + L[j] > L[i]) and (L[i] + L[j] + L[k] > p):
                    p = L[i] + L[j] + L[k]
    print(p)
print(get_largest_perimiter(L))
