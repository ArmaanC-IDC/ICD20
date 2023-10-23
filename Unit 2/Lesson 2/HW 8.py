def calculate_triangle_area(b,h):
    if isinstance(b(int,float)) and isinstance(h(int,float)):
        return b*h/2
    else:
        print("Invalid input. Please provide numeric values")

print(f"the area is {calculate_triangle_area(10,10)}")