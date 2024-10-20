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