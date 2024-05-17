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
