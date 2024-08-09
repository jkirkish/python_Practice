#exceptions help to prevent your program from crashing. this is an example of list index out of range
#https://docs.python.org/3/library/exceptions.html here is a list of all exceptions
#numbers = [1,2]
#print(numbers[3])
#you can use a try except syntax to catch any crashes
try:
   #with open("app.py") as file: # This is the file to open. the 'with" statement automatically closes the file
    #age = int(input("Age: "))#this is the input code for a int value
    age = 78
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

#classes
x =1
print(type(x)) # this prints the class of int, classes for booleans, lists and dictionaries

#class is a blueprint for creating new objects
#Object: instance of a class
class Point: #Pascal naming convention Uppercase first letter and no underscore
   default_color = "red"
       
       
       #__init__(self) the underline twice with init is a special method called the magic method
       #self is a reference to the current point object. put self for at one parameter in python methods
      
   #This init constructor method is automatically called when we have Point object"""
   
   def __init__(self, x, y): #this line of code is a constructor to the python class Point
               self.x = x #instance attributes
               self.y = y #instance attributes
                          #python 3 magin method
   
   
   
   def draw(self): # class functions can have at least one variable name self
       print(f"Point ({self.x}, {self.y})")
   
   """the first parameter cls is a reference to the class itself. 
   @classmethod is a decorator is away to extend the behavior of a method or function"""
   @classmethod  
   def zero(cls):
       return cls(0,0)
    
   def __str__(self):
       return f"({self.x},{self.y})"
   
   def __eq__(self,other):
       return self.x == other.x and self.y == other.y
   
   def __gt__(self,other):
       return self.x > other.x and self.y > other.y
   
   def __add__(self,other):
       return Point(self.x + other.x, self.y + other.y)

point = Point(1,2) # declare a Point object
print(type(point))#this tells you that what type of class point belongs to
print(isinstance(point, Point)) #this returns True a boolean value True or False if variable is an instance of a certain class
print(isinstance(point, int)) # this returns false.

Point.default_color = "yellow"

point = Point(1,2)
point.z = 10 #instance attributes
print(point.x)
print(point.default_color)
print(Point.default_color)
print(point.draw())

# class level attributes are shared across all instances of a class
# if we change their value. The change is visible to all objects of that type
another = Point(3,4)
print(another.default_color)
another.draw()


#create a point object
Point.zero()#method that is defined at the class level

"""https://rszalski.github.io/magicmethods/"""

point = Point(1,2)
print(str(point))

"""point and other are compared to see if they are equal.  They are not in this example
because they are two different object references in memory"""
point = Point(1,2)
other = Point(1,2)
print(point == other)

#a comparison magic method is avaiable to work this.
point = Point(10,20)
other = Point(1,2)
print(point > other)
print(point < other)

# you can define a magic method that will add two values together in a airthmetic 
point = Point(10,20)
other = Point(1,2)
print(f"point is: {point}")
print(f"other is: {other}")
combined = point + other
print(combined.x)
print(combined.y)


#creating a custom class allows you to have more functionality than simple data structures
class TagCloud:
    def __init__(self):
        self.__tags= {}
     #highlight a variable name and push f2 to refactor a new name
     #prefixing an attribute with __attributeName will make it private
     
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getItem__(self,tag):
        return self.__tags.get(tag.lower(),0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        iter(self.__tags)

#using a dictionary case sensitivy comes into play as two different items. 
cloud = TagCloud()
#print(cloud.__tags)
cloud["python"] = 10
cloud.add("Python")
cloud.add("python")
cloud.add("python")

cloud = TagCloud()
print(cloud.__dict__)
print(cloud._TagCloud__tags)

#if something is not pythonic, it is not using the best practices in python
class Product:
    def __init__(self,price):
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

product = Product(10)
print(product.price)



class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def walk(self):
        print("walk")
    

#inheritance (DRY dont' repeat yourself)have inheritance classes that go to one or two levels
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def eat(self):
        print("eat")


class Fish(Animal):
     def swim(self):
        print("swim")


m = Mammal()
m.eat()



m = Mammal()

print(isinstance(m, object))
print(issubclass(Mammal, object))
m.eat()

print(m.age)
print(m.weight)

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

"""multilevel inheritance goes into the order of Employee first, and then person second. You want to be careful 
not to switch the order if you have it a certain way"""
class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()
"""he ABC and abstractmethod are tools provided by Python's abc (Abstract Base Classes) module to define abstract base classes, which are classes that cannot be instantiated directly and are meant to be subclassed. They are useful for defining a blueprint for other classes.

Here's a breakdown of the two:

ABC (Abstract Base Class)
ABC is a base class in the abc module that you use to create abstract classes.
An abstract class is a class that contains one or more abstract methods (methods that are declared but contain no implementation).
Abstract classes cannot be instantiated directly; you can only create instances of their subclasses.
abstractmethod
abstractmethod is a decorator that you apply to methods in a class to mark them as abstract.
An abstract method is a method that is declared in an abstract class but lacks a complete implementation.
Subclasses of an abstract class are required to override all abstract methods. If a subclass does not implement all abstract methods, it also becomes abstract and cannot be instantiated."""
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False
    
    
    @abstractmethod
    def read(self):
        pass

"""a Good level of multilevel inheritance"""
class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")

stream = MemoryStream()
stream.open()

#polymorphism
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")
   
class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(control):
    for control in control:
        control.draw()

ddl = DropDownList()
print(isinstance(ddl, UIControl))


ddl = DropDownList()
textBox = TextBox()
draw([ddl, textBox])


"""Polymorphism in Python refers to the ability of different classes to be treated as instances of the same class through a common interface. It allows for methods to be called on different objects, and the object will determine which implementation of the method to execute.

Types of Polymorphism in Python
Duck Typing:

Python uses a dynamic type system where the type of an object is determined at runtime.
Duck typing is a concept where an object's suitability is determined by the presence of certain methods and properties, rather than the type of the object itself.
The famous saying "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck" explains this idea.Method Overriding:

Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.
The overridden method in the subclass will be called, allowing polymorphic behavior.Function Polymorphism:

In Python, functions can take arguments of different types, leading to different behavior depending on the type of input.
This is not as formalized as method overriding but allows for flexibility in function behavior.Polymorphism is especially useful when you want to write generic code that can work with objects of different types but share the same interface."""

#Extending built-in types
class Text(str):
    def duplicate (self):
        return self + self
    
text = Text("Python")
print(text.duplicate())

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("1")


#Data Classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1,2)
p2 = Point(1,2)
print(id(p1))
print(id(p2))
print(p1 == p2)

from collections import namedtuple
    
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1==p2)