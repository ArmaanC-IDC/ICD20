def multiply(n1, n2):
    if isinstance(n1,(str,float)) and isinstance(n2,(str,float)):
        return n1*n2
    else:
        print("Invalid input, please provide numeric inputs")

n1 = float(input("1st number: "))
n2 = float(input("2nd number: "))
print(f"The product of {n1} and {n2} is {multiply(n1,n2)}")

