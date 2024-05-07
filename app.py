import math

print("Hello World ")
print("*" * 10)
# https: //peps.python.org/pep-008/
print("Hello World")

x = 1

students_count = 1000
rating = 4.99
# boolean values should always start with a capital letter False or True
# Python is a case sensitive language.
# make variable names descriptive and readable
# lowercase letters to name letters
# formatted code properly use pep-008 standards
# use triple quotes """ when you have a long string to format
is_published = False
course = "Python Programming"
print(students_count)
print(len(course))  # return the number of characters 18 in the string
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# escape characters in python
# \"
# \'
# \\
# \n
course = "Python \nProgramming"
print(course)
first = "first Name"
last = "last name"
full = first + " " + last
print(full)
full = f"{first} {last}"  # formatted strings
print(full)
full = f"{len(first)} {2 + 2}"  # formatted strings
print(full)

course = "   python programming"
print(course.upper())
print(course)
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("pro"))  # returns the index
print(course.find("bde"))
print(course.replace("p", "j"))
print("pro" in course)  # returns boolean that it is found within the string
print("swift" not in course)
x = 1
x = 1.1
x = 1 + 2j
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # integers
print(10 % 3)  # modulus
print(10 ** 3)  # exponent

x = 10
x = x + 3  # is the same as
x += 3
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))  # https://docs.python.org/3/library/math.html
input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")
# primitives int, float, bool, strings, None
fruit = "Apple"
print(fruit[1:-1])
