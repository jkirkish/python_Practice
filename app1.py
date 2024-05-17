# New-Item new_file.py -ItemType file
temperature = 35

if temperature > 30:
    print("It is warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

age = 22
if age >= 18:
    message = "is eligible"
else:
    message = "is not eligible"
print(message)
# another way to say this with few code is:
age = 23
message = "is eligible" if age >= 18 else "is not eligible"
print(f"His age {age} {message}")


age = 2
message = "is eligible" if age >= 18 else "is not eligible"
print(f"His age {age} {message}")

# three logical operators and, or, not
high_income = False
good_credit = True
student = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")


if not student:
    print("Student is eligible")
else:
    print("Not eligible")


student = True
if not student:
    print("Student is eligible")
else:
    print("Not eligible")

high_income = True
good_credit = True
student = True
if (high_income or good_credit) and not student:
    print("Student is eligible")

# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")
# for loops
for number in range(3, 10, 2):
    print("Attempt", number + 1, number * ".")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print(type(5))
print(type(range(5)))

# iterable
for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# for item in shopping_cart:
    # print(item)

# while loops
number = 100
while number > 0:
    print(number)
    number //= 2
# infinite loops need to have a way to stop to avoid consuming too much memory
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
