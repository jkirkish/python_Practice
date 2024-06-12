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
