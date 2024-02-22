n = int(input("how many players on team? "))
num_of_40 = 0
for i in range(n):
    p = int(input("points: "))
    f = int(input("fouls: "))
    if (p*5 - f*3)>40:
        num_of_40+=1
if num_of_40==n:
    print(str(num_of_40)+'+')
else:
    print(num_of_40)