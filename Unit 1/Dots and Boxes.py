#getting inputs
name = input("What is your name? ")

#game 1
print("game 1:")
name1 = input("What was your opponent's name? ")
yourboxes1 = input("How many boxes did you get? ")
opponentboxes1 = input("How many boxes did your opponent get? ")

#game 2
print("game 2:")
name2 = input("What was your opponent's name? ")
yourboxes2 = input("How many boxes did you get? ")
opponentboxes2 = input("How many boxes did your opponent get? ")

#game 3
print("game 3:")
name3 = input("What was your opponent's name? ")
yourboxes3 = input("How many boxes did you get? ")
opponentboxes3 = input("How many boxes did your opponent get? ")

#game 4
print("game 4:")
name4 = input("What was your opponent's name? ")
yourboxes4 = input("How many boxes did you get? ")
opponentboxes4 = input("How many boxes did your opponent get? ")

#game 5
print("game 5:")
name5 = input("What was your opponent's name? ")
yourboxes5 = input("How many boxes did you get? ")
opponentboxes5 = input("How many boxes did your opponent get? ")


#outputs
#game 1
print("Game 1:")
print(f"Opponent's Name: {name1}")
print(f"Your Points: {yourboxes1}")
print(f"Opponent's Points: {opponentboxes1}")

#game 2
print("Game 2:")
print(f"Opponent's Name: {name2}")
print(f"Your Points: {yourboxes2}")
print(f"Opponent's Points: {opponentboxes2}")

#game 3
print("Game 3:")
print(f"Opponent's Name: {name3}")
print(f"Your Points: {yourboxes3}")
print(f"Opponent's Points: {opponentboxes3}")

#game 4
print("Game 4:")
print(f"Opponent's Name: {name4}")
print(f"Your Points: {yourboxes4}")
print(f"Opponent's Points: {opponentboxes4}")

#game 5
print("Game 5:")
print(f"Opponent's Name: {name5}")
print(f"Your Points: {yourboxes5}")
print(f"Opponent's Points: {opponentboxes5}")

print(f"Player's Name: {name}")


#table
opponent = "Opponent"
your_points = "Your Points"
opp_points = "Opponent Points"
box_percent = "Box %"


print(f"{opponent:<10}{your_points:>15}{opp_points:>20}{box_percent:>10}")

print("========================================================")
boxpercent1 = int(yourboxes1)/49*100
boxpercent1 = round(boxpercent1,2)
print(f"{name1:<10}{yourboxes1:>15}{opponentboxes1:>20}{boxpercent1:>10}")

boxpercent2 = int(yourboxes2)/49*100
boxpercent2 = round(boxpercent2,2)
print(f"{name2:<10}{yourboxes2:>15}{opponentboxes2:>20}{boxpercent2:>10}")

boxpercent3 = int(yourboxes3)/49*100
boxpercent3 = round(boxpercent3,2)
print(f"{name3:<10}{yourboxes3:>15}{opponentboxes3:>20}{boxpercent3:>10}")

boxpercent4 = int(yourboxes4)/49*100
boxpercent4 = round(boxpercent4,2)
print(f"{name4:<10}{yourboxes4:>15}{opponentboxes4:>20}{boxpercent4:>10}")

boxpercent5 = int(yourboxes5)/49*100
boxpercent5 = round(boxpercent5,2)
print(f"{name5:<10}{yourboxes5:>15}{opponentboxes5:>20}{boxpercent5:>10}")
print("========================================================")

total_points = str(int(yourboxes1)+int(yourboxes2)+int(yourboxes3)+int(yourboxes4)+int(yourboxes5))
total_opp_points = str(int(opponentboxes1)+int(opponentboxes2)+int(opponentboxes3)+int(opponentboxes4)+int(opponentboxes5))
print("Total Points: "+total_points)
print("Total Opponent Points: "+total_opp_points)
points_percent = str(round(int(total_points)/245,2))
print("Percentage of points recieved: "+points_percent)