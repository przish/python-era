"""
Exercise 4: Selection Structures and Booleans (Lesson 6)
Write a conditional block that checks an integer variable a = 25.
⚬	If it is greater than 10 AND less than or equal to 30, print "Valid Range".
⚬	Otherwise, if it is exactly equal to 50, print "Half-century".
⚬	If neither condition is met, print "Out of Range".

Exercise 5: Iterative Structures (Lesson 7)
Using a while loop, iterate through numbers starting from 2 up to 10. Print only the even numbers, but use a control statement to skip the number 6 so it does not get printed.

Exercise 6: Collections (Lesson 8)
Given my_list = [1, 2, 3, 2, 4, 1], perform the following in order:
	1.	Convert the list into a set to automatically remove the duplicate values.
	2.	Convert that set into a tuple.
	3.	Print the length of the resulting tuple.
"""

# exercise 4
a = 25

if a > 10 and a <= 30:
    print("Valid Range")
elif a == 50:
    print("Half-century")
else:
    print("Out of Range")

# exercise 5
x = 2
while (x <= 10):
    if x == 6:
        x += 2
        continue
    print(x)
    x += 2
    
# exercise 6
my_list = [1, 2, 3, 2, 4, 1]

s = set(my_list)
t = tuple(s)
print(len(t))