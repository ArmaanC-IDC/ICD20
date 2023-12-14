import os
def clear():
    os.system('cls')

#1. Print the numbers from 1-100 inclusive
def print_numbers():
    x = 1
    while x<=100:
        print(x)
        x+=1

#2. Print the even numbers from 1 to 500 inclusive
def even_numbers():
    i = 1
    while i<=500:
        if i%2==0:
            print(i)
        i+=1

#3. Print the odd numbers from 1 to 500 inclusive
def odd_nums():
    i = 1
    while i<=500:
        if i%2==1:
            print(i)
        i+=1
    
#4. Print the numbers from 100 to 1 inclusive (i.e. count backwards)
def backward_nums():
    i = 100
    while i>=0:
        print(i)
        i-=1

#5. Print the even numbers from 500 to 1 inclusive (i.e. count backwards)
def backward_even_nums():
    i = 500
    while i>=0:
        if i%2==0:
            print(i)
        i-=1

#6. Print the odd numbers from 500 to 1 inclusive (i.e. count backwards)
def backward_odd_nums():
    i = 500
    while i>=0:
        if i%2==1:
            print(i)
        i-=1

#7. Calculate and print the sum of all the odd numbers from 1 to 100 inclusive
def sum_of_nums():
    print("in the function")
    i = 1
    total = 0
    while i<=100:
        total+=i
        i+=1
    print(total)

#8. Takes in a string and prints the string in reverse order
def backward_string():
    str = input("string? ")
    i = len(str)-1
    total = ''
    while i>=0:
        total += str[i]
        i-=1
    print(total)

#9. Takes in an integer and calculates and prints the factorial of that number
def factorial():
    num = int(input("number? "))
    total = 1
    while num>=1:
        total*=num
        num-=1
    print(total)
clear()
# print_numbers()
# even_numbers()
# odd_nums()
# backward_nums()
# backward_even_nums()
# backward_odd_nums()
# sum_of_nums()
# backward_string()
factorial()