def say_hello(name):
    name = str(name)
    print(f"Hi {name}! How are you?")

n = input("What is your name? ")
say_hello(n)