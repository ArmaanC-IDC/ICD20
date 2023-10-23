import math
def calculate_circle_area(r):
    if isinstance(r,(int,float)):
        print(f"The area is {round(math.pi*r**2,2)}")
    else:
        print("Invalid input. please provide a numeric value")

calculate_circle_area(float(input("radius? ")))