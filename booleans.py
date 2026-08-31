print(bool("Hello"))
print(bool(15))

x = 'hello'
y = 15

print(x, y)
print(bool(x))
print(bool(y))

x = ''
y = 0

print(bool(x))
print(bool(y))

"""
any value is true
except empty strings, zero, null, false
"""

# a built-in function in python
print(isinstance("hello", str))
print(isinstance(20, int))
print(isinstance((1, 2, 3), list))

# what is floor division (//)?
# the // operator rounds down to nearest integer
# so 5 // 2? answer: 2

print(5 // 2)
print(5 // 2.0)
