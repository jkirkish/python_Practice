letters = ["a","b","c"]
matrix = [[0,1],[2,3]]
zeros = [0] * 100
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(chars)
print(len(chars))
print(letters[-1])


letters[0] = "A"
print(letters)
print(letters[0:3])
print(letters[0:])
print(letters[::2])

numbers = list(range(20))
print(numbers[::-1])


numbers = [1,2,3,4,4,4,4,4,4,4,4,4,4]
first, second, *other, last= numbers  #list unpacking
print(first)
print(other)
print(first, last)
print(other)
#same way below
first = numbers[0]
second = numbers[1]
third = numbers[2]


def multiply(*numbers):

    multiply(numbers)

letters = ["a","b","c"]
items = [0,"a"]
for index, letter in enumerate(letters):
    print(index, letter)

#add something to the end of the list
letters.append("d")
#add something in a specifcic index 
letters.insert(0, "-")
print(letters)

#remove something at the end of the list
letters.pop()
#remove the first index value of the list
letters.pop(0)
#remove the first occurrence of b
letters.remove("b")
del letters[0:3] # range of items
letters. clear() # removes everything in the list
print(letters)

letters = ["a","b","c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d")) # trying to get the index that doesn't exist, you get an error

numbers = [3,51,2,8,6]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)

items = [
    ("Product1",10),
    ("Product2", 9),
    ("Product3",12),
]

#def sort_item(item):
    #return item[1]

#items.sort(key=sort_item)
# prices = []
#for items in items:
 #   prices.append(items[1])

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items] #use list comprehensions becuase they are cleaner and more performant 
print(prices)


filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)

list1 = [1 ,2, 3]
list2 = [10, 20, 30]

print(list(zip("abc",list1, list2)))

#LIFO - > last In - First Out stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
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

#QUeues  (FIrst In First Out)
from collections import deque
queue = deque([])
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

#tuples are immutable they are good at preventing errors with adding or removing objects
point = (1,2,3)
print(type(point[0:2]))
x,y,z = point
point = tuple("Hello World")
print(point)

if 10 in point:
    print("exists")

#swapping numbers
x = 10
y = 11

x, y = y, x
a, b = 1, 2

print("x", x)
print("y", y)


#array in python are best when dealing with large sequence of numbers and you encounter 
#performance problems
from array import array

numbers = array("i", [1,2,3])
numbers[0] = 1.0
[1,2,3]
