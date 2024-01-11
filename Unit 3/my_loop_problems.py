import random
#1
def multiples_of_n(n):
    for i in range(n,n*10+1,n):
        print(i)

#2. (uses lists, won't be on test)
def over_10(list):
    for element in list:
        if element>10:
            print(element)

def random_nums(len):
    string=''
    for i in range(len):
        string+=str(random.randint(1,10))
    print(string)

def len_str(str1,str2,str3):
    list = [str1,str2,str3]
    for i in range(3):
        print(max(list, key = len))
        list.remove(max(list,key=len))

def factorial():
    num = int(input("number? "))
    total = 1
    while num>=1:
        total*=num
        num-=1
    print(total)
    
def calculator(operator,num1,num2):
    if operator=="+":
        print(num1+num2)
    elif operator=="-": print(num1-num2)
# multiples_of_n(int(input("n: ")))
# over_10([10,5,20,9])
# random_nums(15)
# len_str("hi", "hello world", "hello")
