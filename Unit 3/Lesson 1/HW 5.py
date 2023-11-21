def str_len(string, front):
    string=str(string)
    l = len(string)
    if l==0:
        return "The string is empty"
    elif front==False:
        return string[l-1:l]
    else:
        return string[0:1]
    
print(str_len("", True))