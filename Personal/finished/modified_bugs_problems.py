print()
while True:
    try:
        n = int(input("how many bugs do you want to input? "))
        if n<=0:
            print("please enter a positive, whole, number")
        else:
            break
    except ValueError:
        print("Invalid input, please enter a number")

bugs_list = []
count_list = []
max_bugs_len = 0
max_count_len = 0
for i in range(n):
    bugs_list.append(input(f"Enter bug {i+1}: "))
    if len(bugs_list[i])>max_bugs_len:
        max_bugs_len = len(bugs_list[i])
    while True:
        try: 
            x = int(input(f"how many {bugs_list[i]}s: "))
            count_list.append(x)
            break
        except ValueError:
            print("Invalid input. Please enter a number")
    if len(str(count_list[i]))>max_count_len:
        max_count_len = len(str(count_list[i]))
print(max_bugs_len)
print(max_count_len)

total = 0
for i in range(n):
    total = total + count_list[i]
print(f"{'Bug Type':<15}{'Count':>15}{'Percent of Total':>20}")
print("="*(max_count_len+max_bugs_len+20))
for i in range(n):
    print(f"{bugs_list[i]:<{max_bugs_len}}{count_list[i]:>{max_count_len}}{count_list[i]/total:>20.2%}")
print("="*max_count_len+max_bugs_len+20)
print(f"{'Total':<15}{total:>15}{'100%':>20}")