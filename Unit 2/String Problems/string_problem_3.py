def last_2(s):
    l=len(s)
    return s[0:l-2] + s[l-1:l] + s[l-2:l-1]

print(last_2("Coding"))