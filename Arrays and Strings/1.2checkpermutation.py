def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    char_set = [0] * 128

    for c in s1:
        char_set[ord(c)] += 1

    for c in s2:
        char_set[ord(c)] -= 1
        if char_set[ord(c)] < 0:
            return False
    return True


def solution2(s1, s2):
    # Without using additional data structure.
    return sorted(s1) == sorted(s2)
    




s1 = "bat"
s2 = "tab"
print(check_permutation(s1, s2))
print(solution2(s1, s2))