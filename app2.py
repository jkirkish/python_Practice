def greet():
    print("Hi there")
    print("Welcome aboard")


greet()

# parameters are inputs that you define for your function
# an argument is an actual value given for a parameter

# greet function with parameters


def greet1(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet1("Mosh", "Hamedani")
greet1("Josh", "Lopez")

# Types of functions
# 1-Perform a task
# 2-Return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
file = open("content.txt", "w")
file.write(message)

# all functions in python return a "None" value
# None is the abscence of a value
# unless you make the function return something
print(greet1("Mosh", "Josh"))
