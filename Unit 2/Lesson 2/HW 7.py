def calculate_power(n, p):
    if isinstance(n,(float,int)) and isinstance(p,(float,int)):
        return n**p
    else:
        print("Invalid Input. Please provide a numeric value")

print(f"10 to the power of 10 {calculate_power(10,10)}")