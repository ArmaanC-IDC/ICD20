d = float(input("How long is your trip in Km? "))
fe = float(input("What is the fuel efficiency of the car (km/l)? "))
fc = float(input("How much does fuel cost right now? "))
p = float(input("How many passangers are there? "))


tf = d/fe
c = tf*fc
print(f"You will use {tf} L of fuel")
print(f"The total cost of fuel is {c}")
print(f"The total cost per passanger is {c/p}")