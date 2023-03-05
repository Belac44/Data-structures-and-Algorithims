def place_queen(perm, size):
    if len(perm) == size:
        print(perm)
        exit()
    
    else:
        for i in range(size):
            if i not in perm:
                perm.append(i)
                if can_be_extended_to_solution(perm):
                    place_queen(perm, size)
                perm.pop()

    return perm


def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


perm = place_queen(perm=[], size = 5)

print(perm)