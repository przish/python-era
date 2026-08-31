print("Hello, world!", end=" ")
print("i love you")

print("I am", 25)
# this is how you print string + int
# this is also how you comment

# Write a single-line comment

# Comment out this line so it does not run:
# This is a comment
# print("This should not run")

# Add a multiline comment

"""
This is
a multiline
comment
"""


# you can name your variable anything but number as first character, hyphen, whitespace
# vars are case sensitive 

"""
camel helloWorld
pascal HelloWorld
snake hello_world
"""

# assigning multivalues

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

print(x, y, z)

# one value to many variables
x = y = z = "hello"

print(x, y, z)

# unpacking

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)
print(x, y, z)

# if automatic merong space, use comma. if not, you can use +. or if you want to combine different data types without encountering errors, use comma.
# using comma is most recommended

x = 5
y = "John"

# print(x + y) output: unsupported operand type(s) for +: 'int' and 'str'
print(x, y)

