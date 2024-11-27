# if __name__ == '__main__':
#     # declare the list my_list as an empty list
#     my_list = []
#     #read the number of commands to put
#     N = int(input())
#     #process each command
#     for _ in range(N):
#         #use the input to separate the command and its arguments
#         command = input().split()
        
#         if command[0] == "insert":#inserts integer e at index i
#             my_list.insert(int(command[1]), int(command[2]))
#         elif command[0] == "print": #prints the first occurrence of e
#             print(my_list)
#         elif command[0] == "remove":#removes the first occurrence of e
#             my_list.remove(int(command[1]))
#         elif command[0] == "append": #appends e at the end of the list
#             my_list.append(int(command[1]))
#         elif command[0] == "sort": #sorts the list in ascending order
#             my_list.sort()
#         elif command[0] == "pop": #removes the last element from the list
#             my_list.pop()
#         elif command[0] == "reverse":#reverses the list
#             my_list.reverse()

# def count_substring_occurrences(original_string, substring):
#     count = 0
#     substring_length = len(substring)
#     original_length = len(original_string)
    
#     # Traverse the original string
#     for i in range(original_length - substring_length + 1):
#         # Check if the substring matches the segment of the original string
#         if original_string[i:i + substring_length] == substring:
#             count += 1
            
#     return count

# # Input
# original_string = input().strip()
# substring = input().strip()

# # Count occurrences and print the result
# result = count_substring_occurrences(original_string, substring)
# print(result)



# thickness = int(input())
# for i in range(thickness):
#     string = 'H'*(i*2+1)
#     print(string.center(thickness*2, ' '))

# for i in range(thickness + 1):
#     string = 'H'*thickness + '   '*thickness + 'H'*thickness   
#     print(string.center(thickness*6, ' '))
    

# for i in range(int((thickness + 1)/2)):
#     string = 'H'*thickness*5      
#     print(string.center(thickness*6, ' '))
    
# for i in range(thickness + 1):
#     string = 'H'*thickness + '   '*thickness + 'H'*thickness
#     print(string.center(thickness*6, ' '))
    
# for i in range(thickness):
#     string = 'H'*((thickness - i - 1)*2 + 1)
#     print(' '*thickness*4 + string.center(thickness*2, ' '))

def print_formatted(number):
    # Calculate the width based on the binary representation of the largest number
    width = len(bin(number)[2:])  # bin(number) returns a string like '0b...' so we slice off the '0b'
    
    for i in range(1, number + 1):
        # Prepare the different representations
        decimal = str(i)
        octal = oct(i)[2:]  # oct(i) returns a string like '0o...'
        hexadecimal = hex(i)[2:].upper()  # hex(i) returns a string like '0x...' and we want uppercase
        binary = bin(i)[2:]  # bin(i) returns a string like '0b...'
        
        # Print the formatted string
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Python Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered. changeable and do not allow duplicates
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thisdict["brand"]) # this prints out "Ford"

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name
#Dictionaries are ordered, it means that the items have a defined order, and that order will not change
#unordered means that the items do not have a defined order, you cannot refer to an item by using an index
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been 
#created

#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key.  
#Duplicate values will overwrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) #this will print out for year 2020

#to determine how many items a dictionary has, use the len() function:
print(len(thisdict)) #this prints out 3

#the values in dictionary items can be of any data type String, int, boolean and list data types
thisdict = {

    "brand": "Ford",
    "electric": False,
    "year": 1964,
     "colors": ["red", "white", "blue"]
}
print(type(thisdict))#Python's perspective dictionaries are defined as objects with the data type 'dict':

#it is also possible to use the dict() constructor to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Python Collections you can access the items of a dictionary by referring to its key name, inside square brackets
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
x = thisdict["model"]
print(x)

#there is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)

#the keys method will return a list of all the keys in the dictionary
x = thisdict.keys()
print(x)
#the list of the keys is a view of the dictionary, meaning that any changes done to the 
#dictionary will be reflected in the keys list. 
#add a new item to the orginal dictionary, and see that the keys list gets updated as well:
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "years" : 1964
}

x = car.keys()
print(x)#before the change

car["color"] = "white"
print(x)

# value() method will return a list of all the values in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
#make a change in the original dictionary, and see that the values lists gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# add a new item to the original dictionary, and see that the values lists get updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)

car["color"] = "red"
print(x)# after the change

#the items() method will return each item in a dictionary as tuples in a list
x = thisdict.items()

# the returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary 
#will be reflected in the items list. 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#check if a key exists in a dictionary use the "in" keyword
thisdict = {
    "brand" : "Ford",
     "model" : "Mustang",
     "year" : 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")


#change values you can change the value of a specific item by referring to its key name:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["year"] = 2018

#the update() method will update the dictionary with the items from the given argument. The
#the argument must be a dictionary, or an iterable object with key:value pairs. 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

#adding items to the dictionary is done by using a new index key and assigning a value to it:
#the update method will update the dictionary with the items from a given argument. If the item
#does not exist, the item will be added.  The argument must be a dictionary, or an iterable object
#with key:value pairs. 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)


#removing items from the dictionary involve several ways
#the pop() method removes the item with the specified key name:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.pop("model")
print(thisdict)

#the popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#the del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#the del keyword can also delete the dictionary completely
del thisdict
#printing the dictionary after it has been deleted will cause an error

#the clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)