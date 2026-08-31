"""
Exercise 1: Fundamentals, Variables, and Typecasting (Lessons 1 & 4)
Create a variable x with the string value "50". Typecast it into an integer, add 10 to it using an assignment operator, and print the result using a string placeholder (like an f-string).

Exercise 2: Operators and String Handling (Lessons 2 & 3)
Given the string txt = " Data Science ", use a built-in method to remove the leading and trailing whitespaces. Then, concatenate it with the string "Rocks" using the arithmetic operator + and print the entire result in uppercase.

Exercise 3: Built-in Libraries (Lesson 5)
Import the appropriate library to handle advanced math. Given the variable num = 16, find its square root using the library's pre-defined method and print the result as an integer.
"""

# Exercise 1

x = "50"
y = int(x)

y += 10

print(f"result: {y}")

# Exercise 2

txt = " Data Science "

remove_lead_trail = txt.strip()
concat = remove_lead_trail + " Rocks"

print(concat.upper())

# Exercise 3

import math

num = 16

sqr = math.sqrt(num)

print(int(sqr))