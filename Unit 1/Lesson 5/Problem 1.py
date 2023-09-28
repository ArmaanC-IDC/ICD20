dr = float(input("Enter the cost of your drink: $"))
a = float(input("Enter the cost of your appetizer: $"))
e = float(input("Enter the cost of your entree: $"))
de = float(input("Enter the cost of your dessert: $"))
t = float(input("Enter the tip rate as a percent: "))

Subtotal = dr+a+e+de
tip = Subtotal*(t/100)
print(f"Subtotal: ${Subtotal}")
print(f"Tip: ${tip}")
print(f"Total: {Subtotal + tip}")