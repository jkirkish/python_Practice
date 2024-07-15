letters = ["a","b","c"]
matrix = [[0,1],[2,3]]
zeros = [0] * 5
#Lists can be combined and do not have to be the same type
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(chars)
print(len(chars))
# this prints the last item in the list "c"
print(letters[-1])

# this will change the first index of letters from "a" to "A"
letters[0] = "A"
print(letters)
#[0:3] this prints the first three letters in the original list
print(letters[0:3])
#[0:] the length of the expression will print out all of letters ["a", "b", "c"]
print(letters[0:])
# this will pass every third element in the list ['A','c']
print(letters[::2])
# this prints a list 0 to 19
numbers = list(range(20))
# this prints a list of all even numbers to 18.  [0,2,4,6,8,10.....]
print(numbers[::2])
# this will print all numbers in reverse order...[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-1])

numbers = [1,2,3]
first, second, third = numbers
# this is known as list unpacking
"""the number of items on the left side of the assignment operator = should be the same as the number of items
in the list. If there is an imbalance of items with the number of variables you would get a variable error"""
first = numbers[0]
second = numbers[1]
third = numbers[2]

numbers = [1,2,3,4,4,4,4,4,4,4,4,4,4]
"""You can unpack first and second values in a list and use *other to put all following values 
in a list called other"""
first, second, *other, last= numbers  #list unpacking
#same way below you can put each index in numbers into a variable name
first = numbers[0]
second = numbers[1]
third = numbers[2]
print(f"First is: {first}")
print(f"second is: {second}")
print(f"Other is: {other}")
print(first, last)
print(other)
#same way below
first = numbers[0]
second = numbers[1]
third = numbers[2]



letters = ["a","b","c"]
items = [0,"a"]
"""you can loop thru the list of letters a,b,c with a normal for loop"""
for letters in letters:
    print(letters)

#you can use enumerate in a for loop that gives you a tuple of the list that is read only
#print("This is a tuple of letter list")
letters = ["a","b","c"]
for letter in enumerate(letters):
    print(letter[0], letter[1])
    

for index, letter in enumerate(letters):
    print(index, letter)

#add something to the end of the list
letters.append("d")
#add something in a specifcic index 
letters.insert(0, "-")
print(f"this is append d and insert - {letters}")

#remove something at the end of the list
letters.pop()
print(f"this pop {letters}")
#remove the first index value of the list
letters.pop(0)
print(f"this pop at index 0 {letters}")
#remove the first occurrence of b
letters.remove("b")
print(f"this is remove b {letters}")
letters = ["a","b","c","d"]
#the del letters can delete a range of values you specify [0:3]
del letters[0:3] # range of items
print(f"the the del letters[0:3] {letters}")
letters = ["a","b","c"]
letters. clear() # removes everything in the list
print(f"this pop and remove and clear {letters}")

letters = ["a","b","c"]
#you can find the index of a certain value in your list
print(f"the index of a is: {letters.index("a")}")


letters = ["a","b","c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d")) # trying to get the index that doesn't exist, 
    #you get an error. You can use an if statement to prevent this.
"""You can use the letters.count(some value here) to find then number of occurrences of that value """
numbers = [3,51,2,8,6]
print(f"this is sorted ascending order: {sorted(numbers)}")# sort your numbers in ascending order
# numbers.sort(reverse=True) to sort the numbers in descending order
print(sorted(numbers, reverse=True))
print(numbers)
"""Sorting a tuple can be done using a function"""
#def sort_item(item):
    #return item[1]


#this is your tuple
items = [
    ("Product1",10),
    ("Product2", 9),
    ("Product3",12),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(f"the sorted tuple on items[1]: {items}")

# a shorter cleaner way to code the sorted tuple items is like this
"""items.sort(key=lamba item: item[1])"""
items.sort(key=lambda item:item[1])
print(f"this is lambda sort: {items}")

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
#you can use a for loop to iterate thru each item
prices = []
for item in items:
    prices.append(item[1])

print(f"this is for loop in item prices: {prices}")    

# there is a better way using a map function
x = map(lambda item: item[1], items)
for item in x:
    print(f"items with map: {item}")
# you can convert a tuple to a list
x = list(map(lambda item: item[1], items))
for item in x:
    print(f"items with map converted to list: {item}")

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# you can filter thru this list
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(f"this is filtered list: {filtered}")

#list comprehensions
"""[expression for item in items]"""
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
#list comprehensions
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >=10]
#use the zip function
list1 = [1 ,2, 3]
list2 = [10, 20, 30]
#use the zip function to combine the lists
#zip function one or more iterables
#[('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc",list1, list2)))

#LIFO - > last In - First Out stacks browsing sessions in browsers use stacks
#a list variable can be used as a stack
browsing_session = []
#this adds one value to the stack browsing_session [1]
browsing_session.append(1)
# same thing browsing_session [1,2]
browsing_session.append(2)
# same thing browsing_session [1,2,3]
browsing_session.append(3)
print(f"browsing session{browsing_session}")
#this removes the last value in browsing session so [1,2,3] becomes [1,2]
last = browsing_session.pop()
print(f"last: {last}")
print(browsing_session)
#browsing_session[-1] this returns the last item
if not browsing_session:
    print("redirect", browsing_session[-1])


#stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]

#stack operations (Lastin Last out)
last = browsing_session.pop()
print(last)
print("redirect",browsing_session[-1])
if not browsing_session:
    print("disable")

#QUeues  (FIrst In First Out - FIFO)
"""you can use a list to act out on a queque. an example of a queque is a bathroom line.
You need to import a queuq from collections in your python file"""
from collections import deque
# declare a queue object 
queue = deque([])
queue = deque([])
#you can use the append method in queues
queue.append(1)
queue.append(2)
queue.append(3)
#you can remove one item from the beginning of the list popleft()
queue.popleft()
print(f"queue is: {queue}")
#you can see if a queque is empty by using an if statement
if not queue:
    print("empty")

#tuples are immutable they are good at preventing errors with adding or removing objects
point = 1, #add a comma and you won't confuse with python with an integer with a single value
point = () # use empty parentheses if you want to have an empty tuple
point = (1,2,3)
print(type(point[0:2]))# you can access a range of items in a tuple or a specific index
x,y,z = point  #you can use a tuple point and assign those values 1,2,3 to x,y,z
print(f"x is: {x}")
print(f"y is: {y}")
print(f"z is: {z}")
#you can assign a String value to a tuple 
point = tuple("Hello World")
print(point)


#swapping numbers requires a third variable
x = 10
y = 11

z = x
print("z", z)
x = y
print("x", x)
y = z
print("y", y)



#this is one way to swap variable with x and y without a third variable and one line of code.
x, y = y, x

print("x one variable", x)
print("y one variable", y)


#array in python are best when dealing with large sequence of numbers and you encounter 
#performance problems
#you have to import array into your python file
from array import array

numbers = array("i", [1,2,3]) #every object in the array should be of the same type as determined by
##https://docs.python.org/3/library/array.html  this website of object identifiers
"""you have several methods you can use in arrays.  
array.remove(index)
array.pop(index)
array.insert(index)
"""
numbers[0] = 1
[1,2,3]

"""Data structure of sets.  A data structure with no duplicates"""
numbers = [1,1,2,3,4]
uniques = set(numbers)
second = {1,4}
second.add(5)
second.remove(5)
len(second)
print(uniques)
"""This is the data structure to use"""
numbers = [1,1,2,3,4]
first = set(numbers)
second = {1,5}
#sets are not ordered and do not support indexing

print(first|second) #union of these two sets
print(first & second) #all intersection of first and second sets 
print(first - second) #the difference of two sets
print(first ^ second) #items of the first or second set but not both

#you can check for the existence of a value in a set
if 1 in first:
    print("yes")

"""dictionary is a data structure that has a key and value pairs"""
point = {"x": 1, "y": 2}
point = dict(x = 1, y =2)
print(f"Point dictionary: {point}")
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])  
print(point.get("a",0))
del point["x"] # deletes x
print(point)
#here is how to iterate thru a dictionary
print("dictionary interation")
for key in point:
    print(key, point[key])
print(f"Point dictionary after z added: {point}")

#here is another way to iterate thru a dictionary
for key, value in point.items():
    print(key, value)

values = []
for x in range(5):
    values.append(x * 2)

#[expression for item in items] this is a comprehension list. 
#comprehensions are not limited to lists. they can be used with sets and dictionaries
values =  [x * 2 for x in range(5)]
values =  {x * 2 for x in range(5)}
print(values)

{1,2,3,4} #this is a set
{1: "a", 2: "b"} # this is a dictionary

#dictionary comprehension list
values = {x: x * 2 for x in range(5)}
print(f"Dictionary is: {values}")
#other data structures
#list()
#tuple()
#set()
#dict()

#values becomes a generator object
from sys import getsizeof #import the size function to get the size of the generator object
values = (x * 2 for x in range(10))
print(values)#this prints out a generator object. they are iterable
for x in values:
    print(x)

values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
#makes this one a list
values = [x * 2 for x in range(100000)]
print("gen:", getsizeof(values))

"""when you want to unpack a list you can use the unpack operator in python"""
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

# how to combined unpacked lists
first = [1,2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

# how to unpack dictionaries 
first = {"x" : 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)