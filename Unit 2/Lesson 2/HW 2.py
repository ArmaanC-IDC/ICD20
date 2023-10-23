import math
def calculate_cyl_volume(r, h):
    if isinstance(r,(str,float)) and isinstance(h,(str,float)):
        return round(math.pi*(r**2)*h,2)
    else:
        print("Invalid input, please provide a numeric input")

r = float(input("Radius: "))
h = float(input("Hight: "))
print(f"the volume is {calculate_cyl_volume(r,h)} square units.")

