import math

print("Hello World ")
print("how are you?")
print("I love learning python")
print("Learning Python is a nice career advancement")
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
print(course[0]) #P
print(course[-1])#g
print(f"should be n:{course[-2]}")#n
print(course[0:3])#Pyt
print(course[0:])#Python Programming
print(course[:3])#Pyt
print(course[:])#Python Programming

# escape characters in python
# \"
# \'
# \\
# \n prints the value or text to the next line 
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
print(course.upper()) #to upper case
print(course)
print(course.lower())# to lower case
print(course.title())# capitalizes the first letter of each word
print(course.rstrip()) #removes the trailing whitespace or any trailing characters end of a string
print(course.find("pro"))  # method in Python is used to search for the first occurrence of a specified substring in a string.
print(course.find("bde"))  # It returns the lowest index where the substring is found. If the substring is not found, it returns -1.
print(course.replace("p", "j")) #method in Python is used to replace occurrences of a specified substring with another substring.
print("pro" in course)  # returns boolean that it is found within the string
print("swift" not in course)
x = 1
x = 1.1
x = 1 + 2j
print(10 + 3)#13
print(10 - 3)#7
print(10 * 3)#30
print(10 / 3)#3.3333333333
print(10 // 3)  # integers 3
print(10 % 3)  # modulus  1
print(10 ** 3)  # exponent 1000

x = 10
x = x + 3  # is the same as
x += 3
print(round(2.9)) #3
print(abs(-2.9)) #2.9
print(math.ceil(2.2))  # https://docs.python.org/3/library/math.html  3
input("x: ")  #input a value from keyboard for x
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")
# primitives int, float, bool, strings, None
fruit = "Apple"
print(fruit[1:-1])
