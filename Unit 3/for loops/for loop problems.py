import os
def clear():
    os.system('cls')

#1. Print the numbers from 1-100 inclusive
def print_numbers():
    for i in range(1,101):
        print(i)

#2. Print the even numbers from 1 to 500 inclusive
def even_numbers():
    for i in range(2,500,2):
        print(i)

#3. Print the odd numbers from 1 to 500 inclusive
def odd_numbers():
    for i in range(1,500,2):
        print(i)

#4. Print the numbers from 100 to 1 inclusive (i.e. count backwards)
def backward_numbers():
    for i in range(100,0,-1):
        print(i)

#5. Print the even numbers from 500 to 1 inclusive (i.e. count backwards)
def even_numbers_backward():
    for i in range(500,1,-2):
        print(i)

#6. Print the odd numbers from 500 to 1 inclusive (i.e. count backwards)
def odd_numbers_backward():
    for i in range(499,1,-2):
        print(i)

#7. Calculate and print the sum of all the odd numbers from 1 to 100 inclusive
def sum_of_odd_nums():
    total = 0
    for i in range(1,101,2):
        total+=i
    print(total)

#8. Takes in a string and prints the string in reverse order
def reverse_order():
    str = input("what is the string? ")
    backward = ''
    for i in range(len(str)-1, -1, -1):
        backward+=str[i]
    print(backward)

#9. Takes in an integer and calculates and prints the factorial of that number
def factorial():
    num = int(input("what is the number? "))
    total = 1
    for i in range(1,num+1):
        total*=i
        print(i)
    print(total)

clear()
# print_numbers()
# even_numbers()
# odd_numbers()
# backward_numbers()
# even_numbers_backward()
# odd_numbers_backward()
# sum_of_odd_nums()
# reverse_order()
factorial()