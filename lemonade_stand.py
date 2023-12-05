import random
def get_weather():
    weather = random.randint(1,5)
    if weather==1:
        weather = "sunny"
    elif weather==2:
        weather = "hot and dry"
    else:
        weather = "cloudy"
    return weather

def customer_calculation(weather):
    if weather=="sunny":
        num_of_customers = random.randint(20,40)
    elif weather=="hot and dry":
        num_of_customers = random.randint(30,50)
    else:
        num_of_customers = random.randint(10,30)
    return num_of_customers

def get_user_inputs(weather):
    print(f"The weater is {weather}")
    print()
    while True:
        try:
            num_of_lemonades = int(input("How many cups of lemonade do you want to make?"))
            if num_of_lemonades>=0:
                break
            else:
                print("Invalid input. The number cannot be negative")
                print()
        except ValueError:
            print("Invalid input. Please input a number")
            print()
    
    while True:
        try:
            num_of_signs = int(input("How many signs do you want to make?"))
            if num_of_signs>=0:
                break
            else:
                print("Invalid input. The number cannot be negative")
                print()
        except ValueError:
            print("Invalid input. Please input a number")
            print()

    return num_of_lemonades, num_of_signs

def get_price(weather):
    if weather=="cloudy": price = random.randint(5,15)
    elif weather=="sunny": price = random.randint(15,25)
    elif weather=="hot and dry": price = random.randint(25,35)
    return price

def get_profit(lemonade_cups, signs, customer_num, price):
    if lemonade_cups>=customer_num:
        print("first")
        return (customer_num*price)-(lemonade_cups*2)-(signs*15)
    else:
        print("second")
        return (lemonade_cups*price)-(lemonade_cups*2)-(signs*15)
    
def main():
    total = 0
    while True:
        weather = get_weather()
        lemonade_cups, signs = get_user_inputs(weather)
        customer_num = customer_calculation(weather)
        price = get_price(weather)
        day_profit = get_profit(lemonade_cups, signs, customer_num, price)
        print(f"you made {day_profit} cents")
        total+=day_profit
        print(f"your total profit is {total}")
main()