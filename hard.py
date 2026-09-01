import math

"""
Exercise 7: Nested Logic and Control Statements (Lessons 6 & 7)
Create a nested for loop that iterates through two lists: adj = ["red", "big"] and fruits = ["apple", "banana", "cherry"]. If the adjective is "red" and the fruit is "banana", use a loop control statement to skip printing that specific combination. Otherwise, print the adjective and the fruit together.

Exercise 8: Comprehensive Data Handling (Lessons 1, 3, 4, 7, 8)
Write a short script that simulates user input: user_input = "10, 20, 30".
Split this string into a list of individual strings. Create a loop that iterates through this new list, strips any extra spaces, typecasts each element to an integer, adds 5 to it, and appends the new value to an empty list called updated_numbers. Finally, print updated_numbers.

Exercise 9: Full Integration (Lessons 5, 6, 7)
You have a list of system scores: scores = [45, 88, 92, -5, 105, 77]. Write a for loop to evaluate them:
⚬	If a score is less than 0 or greater than 100, the data is corrupted. Use a statement to immediately stop the entire loop.
⚬	For valid scores, if it is >= 75, print "[Score] - Passed".
⚬	If a valid score is < 75, use a math function (like math.floor) to divide the score by 10 and round it down, then print "[Result] - Failed".
"""

# exercise 7
adj = ["red", "big"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for f in fruits:
        if a == "red" and f == "banana": continue
        print(a, f)

print()
# exercise 8
user_input = "10, 20, 30"

raw_list = user_input.split(',')
updated_numbers = []

for i in raw_list:
    cleaned_item = i.strip()
    value = int(cleaned_item) + 5
    updated_numbers.append(value)

print(updated_numbers)

print()
# exercise 9
scores = [45, 88, 92, -5, 105, 77]

for i in scores:
    if i < 0 or i > 100:
        break
    elif i >= 75:
        print(f"{i} - Passed")
    else:
        result = math.floor(i/10)
        print(f"{result} - Failed")
