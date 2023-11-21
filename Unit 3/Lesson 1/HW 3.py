def squirrel_play(temp, is_summer):
    if is_summer:
        return (temp>=60 and temp<=100)
    else:
        return (temp>=60 and temp<=90)
    
temp = int(input("What temp is it? "))
is_summer = bool(input("Is it summer? answer with 'True' or 'False' "))
print(squirrel_play(temp,is_summer))