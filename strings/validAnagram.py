def validAnagram(s,t):
    if len(s) != len(t):
        return False
    d1 = dict()
    d2 = dict()
    for char in s:
        d1[char] = d1.get(char, 0) + 1
    for char in t:
        d2[char] = d2.get(char, 0) + 1
    return d1 == d2