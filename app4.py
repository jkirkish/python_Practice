#exceptions help to prevent your program from crashing. this is an example of list index out of range
#https://docs.python.org/3/library/exceptions.html here is a list of all exceptions
#numbers = [1,2]
#print(numbers[3])
#you can use a try except syntax to catch any crashes
try:
   with file = open("app.py") # This is the file to open. the 'with" statement automatically closes the file
    age = int(input("Age: "))#this is the input code for a int value
    xfactor = 10/age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)#variable name for value error
    print(type(ex))#print out the error type
else:
    print("No Execeptions were thrown.")
#finally:
    #file.close()# always close the file
print("Execution continues.")


def calculate_xfactor(age):
   if age <= 0:
      raise ValueError("Age cannot be 0 or less.")
   return 10 / age

try:
   calculate_xfactor(-1)
except ValueError as error:
   print(error)

