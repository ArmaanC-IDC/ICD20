# Function to calculate the area of a rectangle
def area_of_rectangle(l, w):
    if isinstance(l, (int, float)) and isinstance(w, (int, float)):
        return l * w
    else:
        print("Invalid input. Please provide three floating-point numbers.")

# Function to check if a string contains a specific substring
def contains_substring(s, ss):
   s = str(s)
   ss = str(ss)
   return ss in s

# Function to calculate the average of three floats
def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x, float) for x in [num1, num2, num3]):
        return (num1 + num2 + num3) / 3.0
    else:
        return "Invalid input. Please provide x floating-point numbers."

# Function to concatenate two strings
def concatenate_strings(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    return str1+str2

# Function to calculate the volume of a cube
def volume_of_cube(side_length):
    if isinstance(side_length, (int, float)):
        return side_length ** 3

# Function to check if a number is positive, negative, or zero
def check_number_status(number):
    if isinstance(number, (int, float)):
        if number > 0:
            return "Positive"
        elif number < 0:
            return "Negative"
        else:
            return "Zero"

# Function to calculate the circumference of a circle
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * 3.141592653589793 * radius

# Function to count the number of occurrences of a character in a string
def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) == 1:
        return string.count(char)

# Function to calculate the percentage of a number
def calculate_percentage(number, percentage):
    if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
        return (percentage / 100) * number

# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)

# Function to capitalize the first letter of a string
def capitalize_first_letter(string):
    if isinstance(string, str):
        return string.capitalize()

# Function to calculate the square of a number
def square(number):
    if isinstance(number, (int, float)):
        return number ** 2

# Function to find the maximum of two numbers
def max_of_two(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        if num1 > num2:
            return num1
        else:
            return num2

# Function to calculate the square root of a number
def square_root(number):
    if isinstance(number, (int, float)) and number >= 0:
        return number ** 0.5

# Function to find the length of a string
def length(input_data):
    if isinstance(input_data, str):
        return len(input_data)
    


#HW 1
x = float(input("enter the length: "))
y = float(input("enter the width: "))
print(f"the area is {area_of_rectangle(x, y):.2f} square units")
print()

#HW 2
s = input("enter the string: ")
ss = input("enter the substring: ")
print(f"is it present? {contains_substring(s, ss)}")
print()

#HW 3
n1 = float(input("enter number 1: "))
n2 = float(input("enter number 2: "))
n3 = float(input("enter number 3: "))
average = round(average_of_three_floats(n1,n2,n3),2)
print(f"the average is {average}")
print()

#HW 4
s1 = input("enter the 1st string: ")
s2 = input("enter the 2nd string: ")
print (f"together, that would be {concatenate_strings(s1, s2)}")
print()

#HW 5
sl = float(input("what is the side length? "))
print(f"The volume is {float(volume_of_cube(sl)):.2f}")
print()

#HW 6
n = float(input("What is the number?"))
print(f"{n} is {check_number_status(n)}")
print()

#HW 7 
r = float(input("what is the radius? "))
print(f"The circumfrence is {float(circumference_of_circle(r)):.2f}")
print()

#HW 8
string = input("What is the string? ")
c = input("What is the character? ")
print(f"{c} appears in {string} {count_char_occurrences(string,c)} times")
print()

#HW 9
number = float(input("enter the number: "))
percent = float(input("enter the percent: "))
print(f"{percent} percent of {number} is {float(calculate_percentage(number, percent)):.2f}")
print()

#HW 10
number1 = float(input("enter a number: "))
number2 = float(input("enter a number: "))
print(f"the absolute difference between {number1} and {number2} is {int(absolute_difference(number1, number2)):.2f}")