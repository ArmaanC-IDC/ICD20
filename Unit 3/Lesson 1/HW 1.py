def caught_speeding(speed,is_birthday):
    if (is_birthday and speed<=65) or (is_birthday==False and speed<=60):
        return "No ticket"
    if (is_birthday and speed>65 and speed<=85) or (is_birthday==False and speed>=60 and speed<=80):
        return "Small ticket"
    if (is_birthday and speed>85) or (is_birthday==False and speed>80):
        return "Big ticket"
        
        
s = int(input("Speed: "))
birthday = bool(input("Is it your b-day? enter with 'True' or 'False'"))
x = caught_speeding(s,birthday)
print(x)