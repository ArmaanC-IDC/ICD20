'''while True:
    try:
        n = int(input("how many peppers? "))
        break
    except ValueError:
        print("Invalid input, please input a non-decimal number")

pepper_list = []
pepper = ""
looping = True
for i in range(n):
    pepper = input("Which pepper would you like to add next? ")
    pepper_list.append(pepper)

t = 0
for pepper1 in pepper_list:
    pepper1 = pepper1.lower()
    if pepper1=="poblano": 
        t+=1500
    elif pepper1=="mirasol": 
        t+=6000
    elif pepper1=="serrano": 
        t+=15500
    elif pepper1=="cayenne": 
        t+=40000
    elif pepper1=="thai": 
        t+=75000
    elif pepper1=="habanero": 
        t+=125000
print(t)

list = [1, 2, 3, 4]
print(list)
'''


def pricing(cups_lemonade,cup_price):
    if cups_lemonade>50 or cups_lemonade<3:
        return "invalid input please try again."
    if cup_price>50 or cup_price<3:
        return "be reasonable with your pricing"
    return cups_lemonade,cup_price

print(pricing(61, 80))