def middle_three(s):
    l=len(s)//2
    return s[l-1:l+2]

print(middle_three("hello world"))