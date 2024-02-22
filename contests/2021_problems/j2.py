n = int(input("how many people"))
highest = [0,'']
for i in range(n):
	name = input("name: ")
	amount = int(input("amount they bid: "))
	if amount>highest[0]:
		highest = [amount, name]

print(highest[1])