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
    #print(user[id])
    print(user["name"])
    #print(user[age]) # type: ignore


save_user(id=1, name="John", age=22)
# {'id': 1, 'name': 'John', 'age': 22} this is a dictionary

# (2,3,4,5) is a tuple
# [2,3,4,5] is a list

# best practice is create functions with local variables.  Global variables only use them
# if you have too.
# F9 is used to add a breakpoint
# f5 opens the integreated terminal

# Examples of bool() function behavior with different inputs

# Empty string -> False
print("Empty string:", bool(""))  # False

# Non-empty string -> True
print("Non-empty string:", bool("hello"))  # True

# Integer 0 -> False
print("Integer 0:", bool(0))  # False
# Examples of bool() function behavior with different inputs

# Empty string -> False
print("Empty string:", bool(""))  # False

# Non-empty string -> True
print("Non-empty string:", bool("hello"))  # True

# Integer 0 -> False
print("Integer 0:", bool(0))  # False

# Positive integer -> True
print("Positive integer:", bool(100))  # True

# Negative integer -> True
print("Negative integer:", bool(-1))  # True

# Empty list -> False
print("Empty list:", bool([]))  # False

# Non-empty list -> True
print("Non-empty list:", bool([1, 2, 3]))  # True

# Empty tuple -> False
print("Empty tuple:", bool(()))  # False

# Non-empty tuple -> True
print("Non-empty tuple:", bool((1, 2)))  # True

# Empty dictionary -> False
print("Empty dictionary:", bool({}))  # False

# Non-empty dictionary -> True
print("Non-empty dictionary:", bool({"key": "value"}))  # True

# None -> False
print("None:", bool(None))  # False

# Float 0.0 -> False
print("Float 0.0:", bool(0.0))  # False

# Non-zero float -> True
print("Non-zero float:", bool(3.14))  # True

# Boolean False -> False
print("Boolean False:", bool(False))  # False

# Boolean True -> True
print("Boolean True:", bool(True))  # True

# Positive integer -> True
print("Positive integer:", bool(100))  # True

# Negative integer -> True
print("Negative integer:", bool(-1))  # True

# Empty list -> False
print("Empty list:", bool([]))  # False

# Non-empty list -> True
print("Non-empty list:", bool([1, 2, 3]))  # True

# Empty tuple -> False
print("Empty tuple:", bool(()))  # False

# Non-empty tuple -> True
print("Non-empty tuple:", bool((1, 2)))  # True

# Empty dictionary -> False
print("Empty dictionary:", bool({}))  # False

# Non-empty dictionary -> True
print("Non-empty dictionary:", bool({"key": "value"}))  # True

# None -> False
print("None:", bool(None))  # False

# Float 0.0 -> False
print("Float 0.0:", bool(0.0))  # False

# Non-zero float -> True
print("Non-zero float:", bool(3.14))  # True

# Boolean False -> False
print("Boolean False:", bool(False))  # False

# Boolean True -> True
print("Boolean True:", bool(True))  # True



n = int(input())
words = [input().strip() for _ in range(n)]
word_count = {}
order_of_appearance = []

for word in words:
    if word not in word_count:
        word_count[word] = 1
        order_of_appearance.append(word)
    else:
        word_count[word] += 1

print(len(order_of_appearance))
print(" ".join(str(word_count[word]) for word in order_of_appearance))


