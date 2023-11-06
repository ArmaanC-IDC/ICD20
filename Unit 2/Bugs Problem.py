#Asks the user to input how many of a bug type there is
def input_bug_counts(bug_type):
    return int(input(f"How many {bug_type}s are there?"))

#Calculates as a percent of the total
def calculate_percent(total,count):
    return (count/total)

#Asks the user to input what a bug type is, and calls the function "input_bug_count" (first funciton)
def input_bug_type_and_count():
    t = input("Enter the type of bug: ")
    c = input_bug_counts(t)
    return t,c

#Displays the table
def display_table(bug1, count1, bug2, count2, bug3, count3):
    t=count1+count2+count3
    print(f"{'Bug Type':<10}{'Count':>10}{'Percent of Total':>20}")
    print("="*40)
    print(f"{bug1:<10}{count1:>10}{calculate_percent(t,count1):>20.2%}")
    print(f"{bug2:<10}{count2:>10}{calculate_percent(t,count2):>20.2%}")
    print(f"{bug3:<10}{count3:>10}{calculate_percent(t,count3):>20.2%}")
    print("="*40)
    print(f"{'Total':<10}{t:>10}{'100%':>20}")

print()
bug1,count1 = input_bug_type_and_count()
bug2,count2 = input_bug_type_and_count()
bug3,count3 = input_bug_type_and_count()

display_table(bug1,count1,bug2,count2,bug3,count3)