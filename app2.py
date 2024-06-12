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


def increment(number, by):
    return number + by


# here shows a keyword argument to make the parameters more clearer increment2 by 1
print(increment(2, by=1))

# default arguments


def increment1(number, by=1):
    return number + by


print(increment1(2))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    print(user)
    print(user[id])
    print(user["name"])
    print(user[age])


save_user(id=1, name="John", age=22)
# {'id': 1, 'name': 'John', 'age': 22} this is a dicitionary

# (2,3,4,5) is a tuple
# [2,3,4,5] is a list

# best practice is create functions with local variables.  Global variables only use them
# if you have too.
# F9 is used to add a breakpoint
# f5 opens the integreated terminal



