'''def extra_front(s):
    return 3*s[0:2]

print(extra_front("Hello"))'''

def last_3_letters(s):
    if isinstance (s, str):
        a = len(s)
        return s[a-3:a]
    
print(last_3_letters(input("string: ")))

