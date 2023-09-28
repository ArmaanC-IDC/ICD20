l=float(input("What is the length of your wall? "))
w=float(input("What is the width of your wall? "))
h=float(input("How tall is your house? "))
c=float(input("How much does a brick cost? $"))
bl=float(input("How long is your brick? "))
bw=float(input("How wide is your brick? "))
bh=float(input("How tall is your brick? "))

fwsa = (l*h)*2
swsa = (w*h)*2
wsa = fwsa + swsa
bsa = bl*bh*bw
b_required = round(wsa/bsa, 0)
b_cost = b_required*c
print()
print(f"The wall area is {wsa} meters cubed")
print(f"You will need {b_required} bricks.")
print(f"This will cost ${b_cost}.")