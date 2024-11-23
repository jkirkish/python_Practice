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
thisset = {"apple","banana","cherry","True",1,2}
print(thisset)
