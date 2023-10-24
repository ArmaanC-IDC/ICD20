def print_triangle(c,h):
    for _ in range(h):
        print(f"{h*c}")
        h = h-1

a=input("character: ")
b=int(input("intager number: "))
print_triangle("a",b)


