print()
bug1,bug2,bug3 = input("What type of bug is the 1st one?"),input("What type of bug is the 2nd one?"),input("What type of bug is the 3rd one?")
count1,count2,count3 = int(input(f"How many {bug1}s are there?")), int(input(f"How many {bug2}s are there?")), int(input(f"How many {bug3}s are there?")),
print(f"{'Bug Type':<10}{'Count':>10}{'Percent of Total':>20}")
print("="*40)
print(f"{bug1:<10}{count1:>10}{count1/count1+count2+count3:>20.0%}")
print(f"{bug2:<10}{count2:>10}{count2/count1+count2+count3:>20.0%}")
print(f"{bug3:<10}{count3:>10}{count3/count1+count2+count3:>20.0%}")
print("="*40)
print(f"{'Total':<10}{count1+count2+count3:>10}{'100%':>20}")