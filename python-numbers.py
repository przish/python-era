x = 1
y = 2.8
z = 1j

print(float(x))
print(int(y))
print(complex(x))
print(complex(y))

import random

print(random.randrange(2, 10))

# is this inclusive? answer: no
# both exclusive? answer: yes

"""
when type casting from float to int, keep in mind that it will not round up
yes, weird.
"""

x = 2.5

print("Example:", end=" ")
print(int(x))