n = int(input("how many peppers? "))
shu = 0
for i in range(n):
    pepper = input("pepper: ")
    if pepper.lower()=='poblano': shu+=1500
    elif pepper.lower()=='mirasol': shu+=6000
    elif pepper.lower()=='serrano': shu+=15500
    elif pepper.lower()=='cayenne': shu+=40000
    elif pepper.lower()=='thai': shu+=75000
    elif pepper.lower()=='habanero': shu+=125000
print(shu)