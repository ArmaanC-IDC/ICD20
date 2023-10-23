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

print(f"Player's Name: {name}")


#Table Calculations
opponent = "Opponent"
your_points = "Your Points"
opp_points = "Opponent Points"
box_percent = "Box %"

#game 1
boxpercent1 = int(yourboxes1)/49*100
boxpercent1 = round(boxpercent1,2)

#game 2
boxpercent2 = int(yourboxes2)/49*100
boxpercent2 = round(boxpercent2,2)

#game 3
boxpercent3 = int(yourboxes3)/49*100
boxpercent3 = round(boxpercent3,2)

#game 4
boxpercent4 = int(yourboxes4)/49*100
boxpercent4 = round(boxpercent4,2)

#game 5
boxpercent5 = int(yourboxes5)/49*100
boxpercent5 = round(boxpercent5,2)

#totals
total_points = int(yourboxes1)+int(yourboxes2)+int(yourboxes3)+int(yourboxes4)+int(yourboxes5)
total_opp_points = int(opponentboxes1)+int(opponentboxes2)+int(opponentboxes3)+int(opponentboxes4)+int(opponentboxes5)
points_percent = round(int(total_points)/245,2)

print()
print(f"{'Opponents':<10}{'Your Points':>15}{'Opponent Points':>20}{'Box %':>10}")
print("========================================================")
print(f"{name1:<10}{yourboxes1:>15}{opponentboxes1:>20}{boxpercent1:>10}")
print(f"{name2:<10}{yourboxes2:>15}{opponentboxes2:>20}{boxpercent2:>10}")
print(f"{name3:<10}{yourboxes3:>15}{opponentboxes3:>20}{boxpercent3:>10}")
print(f"{name4:<10}{yourboxes4:>15}{opponentboxes4:>20}{boxpercent4:>10}")
print(f"{name5:<10}{yourboxes5:>15}{opponentboxes5:>20}{boxpercent5:>10}")
print("========================================================")
print()

#summary
print("Summary")
print(f"Total Points: {total_points}")
print(f"Total Opponent Points: {total_opp_points}")
print(f"Percentage of points recieved: {points_percent:.2%}")