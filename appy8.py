import string

# def print_rangoli(size):
#     lowercase = list(string.ascii_lowercase)
#     required_char = [lowercase[i] for i in range(size)]
#     half_ans = []
    
    
#     for j in required_char:
#         ele = ""
        
#         for x in range(size-1, lowercase.index(j), -1):
#             ele += lowercase[x]
        
#         half_ans.append("-".join(ele + j + ele[::-1]))


#     bottom_half = [h.center(len(half_ans[0]), "-") for h in half_ans]
#     top_half = [h.center(len(half_ans[0]), "-") for h in half_ans[-1:0:-1]]
#     result = top_half + bottom_half
        
#     print(*result, sep='\n')


# print_rangoli(3)
# def first_non_repeating_char(s):
#     # Step 1: Count frequency of each character
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#         print(f"Processed '{char}': {char} count is now {char_count[char]}")  # Print character and its new count
    
#     # Step 2: Find the first character with a count of 1
#     print("\nFinding the first non-repeating character...")
#     for char in s:
#         if char_count[char] == 1:
#             print(f"First non-repeating character found: '{char}'")
#             return char
    
#     # Step 3: Return "_" if no unique character found
#     print("No non-repeating character found. Returning '_'")
#     return "_"

# # Test the function
# first_non_repeating_char("swiss")

# n = int(input())
# words = [input().strip() for _ in range(n)]

# word_count = {}
# order_of_appearance = []

# for word in words:
#     if word not in word_count:
#         word_count[word] = 1
#         order_of_appearance.append(word)
#     else:
#         word_count[word] += 1
        
# print(len(order_of_appearance))

# print(" ".join(str(word_count[word]) for word in order_of_appearance))


#a set is a collection that unordered, unchangeable, unindexed
myset = {"apple","banana", "cherry"}
print(myset)

# The values of True and 1 are considered the same value in sets, and are treated as duplicates
thisset = {"apple","banana","cherry",True,1,2}
print(thisset)

thisset = {"apple","banana","cherry",True,False,0}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#a set with strings, integers, bolean values
set1 = {"abc",34,True,40,"male"}

myset = {"apple","banana", "cherry"}
print(type(myset))

#use the set() constructor to make a set
thisset = set(("apple","banana","cherry")) #note the double round-brackets
print(thisset)

thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)
#check if banana is present
thisset = {"apple","banana","cherry"}
print("banana" in thisset)

#check if banana is NOT present
thisset = {"apple","banana","cherry"}
print("banana" not in thisset)

#add an item to a set use the add() method
thisset = {"apple", "banana","cherry"}
thisset.add("orange")
print(thisset)

#to add items from another set into the current set,use the update() method. 
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}

thisset.update(tropical)
print(thisset)

#add any iterable with tuples, lists, dictionaries
thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]

thisset.update(mylist)

print(thisset)

#to remove an item from a set use the remove() item. 
#if the item to remove does not exist, remove() will raise an error
thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

#you can remove an item in a set using the discard() method
#if the item to remove does not exist, discard() will not raise an error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#you can also use the pop() method to remove an item, but this method removes a 
#random item, so you cannot be sure what item that gets removed
#sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple","banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# the clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#the del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#there are several ways to join two or more sets in Python
#the union() and update() methods joins all items from both sets
#intersection() method keeps ONLY the duplicates
#difference() method keeps the items from the first set that are not in the other sets
# symmetric_difference() method keeps all items EXCEPT the duplicates

#the union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#you can use the | operator instead of the union() method, and you get the same result
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | (set2)
print(set3)

#you can also join multiple sets with the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#the union() method allows you to join a set with other data types, like
#lists or tuples. The result will be a set. 
#The  | operator only allows you to join sets with sets, and not with 
# other data types like you can with the  union() method.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

"""The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.
Both union() and update() will exclude any duplicate items."""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#The intersection() method will return a new set, that only contains 
# the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#You can use the & operator instead of the intersection() method, and you will get the same result.
#The & operator only allows you to join sets with sets, and not with other data types like you can 
# with the intersection() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the 
# original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)

#The difference() method will return a new set that will contain only the items from 
# the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.
#The - operator only allows you to join sets with sets, and not with other data types like you can 
# with the difference() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)


#The difference_update() method will also keep the items from the first set that are not in the 
# other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#The ^ operator only allows you to join sets with sets, and not with other data types like you can with the 
# symmetric_difference() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

# print(set1)

# Method	Shortcut	Description
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others