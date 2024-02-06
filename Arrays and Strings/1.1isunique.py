'''
Implement an algorithm if a string has all unique characters. What if you cannot use additional data strcutures?
'''

def isUnique(s: str):
    # if a string has ASCII values and we can use additional data structure. 
    if len(s) > 128:
        return False
    char_set = [False] * 128
    for c in s:
        if char_set[ord(c)]:
            return False
        else:
            char_set[ord(c)] = True
                 
    return True

def isUniqueWoDs(s: str):
    # If a string is ASCII values and need not use additional data structures.
    if len(s) > 128:
        return False
    sorted_string = sorted(s)
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    return True
    
s1 = "hello world!"
s2 = "teja"
print(isUnique(s1))
print(isUnique(s2))
print(isUniqueWoDs(s1))
print(isUniqueWoDs(s2))
