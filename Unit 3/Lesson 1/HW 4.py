def in1020(a,b):
    if (a>=10 and a<=20) or (b>=10 and b<=20):
        return True
    else:
        return False

a = int(input("What is num 1? "))
b = int(input("What is num 2? "))
print(in1020(a,b))