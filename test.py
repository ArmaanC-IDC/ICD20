n = int(input("Enter number of peppers Ron has put into the chilli: "))

poblano = 1500
mirasol = 6000
serrano = 15500
cayenne = 40000
thai = 75000
habanero = 125000

total_heat = 0

for i in range(n):
    input = input("Enter the name of the pepper Ron has used: ")
    if input == "poblano":
        sum_of_chili = total_heat + poblano
    elif input == "mirasol":
        sum_of_chili = total_heat + mirasol
    elif input == "serrano":
        sum_of_chili = total_heat + serrano
    elif input == "cayenne":
        sum_of_chili = total_heat + cayenne
    elif input == "thai":
        sum_of_chili = total_heat + thai
    elif input == "habanero":
        sum_of_chili = total_heat + habanero
    else:
        break

total = total_heat
print(sum_of_chili)