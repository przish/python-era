a = "Hello, World!"
print(a[1], "\n")

# how to loop in a string?
a = "irish"
for x in a:
    print(x)

print()
print(len(a))

# checking string

print()
print("rain" in a)
print("ish" in a)

if "rain" in a:
    print("oh, yes!")
else:
    print("no, bro")

# if not

if "rain" not in a:
    print("wala")
else:
    print("nandito")

# slicing string
b = "Hello, World!"
print(b[2:5]) # inclusive : exclusive

# from the start
print(b[:5]) # exclusive

# from the end
print(b[2:]) # inclusive


# negative indexing (opposite of start and end)
print(b[-2:]) # exclusive
print(b[:-5]) # exclusive


# modifying string | upper, lower, strip, replace, and split

x = "hello, jopay!"
print(x.upper()) #changes to upper case
print(x.lower()) #changes to lower case
print(x.strip())
print(x.replace("j", "w"))
print(x.split(','))

# concat

a = "hello"
b = "jops"

print(a + b)
print(a + " " + b)

# how to format strings?

# f-string
print(f"hello, {b}")

# the {b} is a placeholder
# it may contain python codes, such as math equations, etc.
n = 2
print(f"number: {n:.2f}")

x = 5
y = 2
print(f"answer: {x / y:.2f}")

x = 50000
print(f"thousand: {x:,}")