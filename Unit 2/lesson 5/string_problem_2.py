def last_chars(a,b):
    l=len(b)
    return a[0:1]+b[l-1:l]

print(last_chars("yo","java"))