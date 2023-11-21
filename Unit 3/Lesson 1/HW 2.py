def not_string(s):
    if s[0:3] == "not":
        return s
    else:
        return "Not " + s
s = input("what is the string? ")
print(not_string(s))