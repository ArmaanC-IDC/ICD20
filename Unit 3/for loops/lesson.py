import os
import time

def clear():
    os.system('cls')

def example():
    for count in range(1,6,0.1):
        print(count)
        #time.sleep(1)

def example_a():
    for count in range(10):
        print(count)

def example_b(start,finish):
    total = 0
    for i in range(start,finish+1):
        total+=i
    return total

def example_c():
    for i in range(10,0,-1):
        print(i)

def example_d(str):
    result = ''
    for i in range(len(str)-1,-1,-1):
        result += str[i]
    print(result)

def example_e(str, n):
    for i in range(0,len(str)-n+1):
        print(str[i:i+n])

def example_f(str1, str2):
    if len(str2)>len(str1):
        return 0   
    result = 0
    for i in range(0,len(str1)-len(str2)+1):
        if str1[i:i+len(str2)] == str2:
            result+=1
    return result

clear()
# example()
# print()
# example_a()
# print()
# print(example_b(int(input("start? ")), int(input("end? "))))
# example_c()
# example_d("abcd")
# example_e("Hello!", 5)
print(example_f("HellohHellow", "y"))