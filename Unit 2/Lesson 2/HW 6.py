def print_square(c,h):
    if isinstance(h(int,float)):
        c = str(c)
        n = h
        while n>0:
            print(f"{c*h}")
            n = n-1
    else:
        print("Invalid input. Please provide a numeric value")

print_square("5",10)
