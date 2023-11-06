def input_bug_counts(bug_type):
    while True:
        try:
            x = int(input(f"How many {bug_type}s are there? "))
            if x>=1000000000:
                print("Invalid input. Number is to big. Please enter a number under 10 digits")
            else:
                return x
        except ValueError:
            print("Invalid Input. Please input only integer")
    
def calculate_percent(total,count):
    return (count/total)

def input_bug_type_and_count():
        while True:
            t = input(f"Enter the type of bug: ")
            c = input_bug_counts(t)
            if len(t)>8:
                print("Name is to long")
            else:
                break
        return t,c

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
while True:
    bug1,count1 = input_bug_type_and_count()
    bug2,count2 = input_bug_type_and_count()
    bug3,count3 = input_bug_type_and_count()
    if count1+count2+count3 == 0:
        print("Everything cannot be 0")
    else:
        break
display_table(bug1,int(count1),bug2,int(count2),bug3,int(count3))