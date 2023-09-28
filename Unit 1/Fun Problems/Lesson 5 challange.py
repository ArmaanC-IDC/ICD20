#challange 1 (give an amount, I will tell you how many of each coin)

m2 = float(input("Input an amount $"))

#toonies
t = m2//2
m = round(m2%2,2)

#loonies
l = m//1
m = round(m%1,2)

#Quarters
q = m//0.25
m = round(m%0.25,2)

#Dime
d = m//0.1
m = round(m%0.1,2)

#Nickel
n = m//0.05
m = round(m%0.05,2)

#Penny
p = m//0.01
print(f"There are {int(t)} toonies, {int(l)} loonies, {int(q)} quarters, {int(d)} dimes, {int(n)} nickels, and {int(p)} pennies, in {m2}")


