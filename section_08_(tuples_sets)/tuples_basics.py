# Tuples: lists that can't change

# A tuple looks like a list, but with parentheses instead of square brackets.
# The big difference: once you make a tuple, you can't change it.
# (That's called "immutable" -- lists are "mutable".)

coordinates = (10, 20)
print(coordinates)
print(coordinates[0])  # indexing works just like a list

# This would crash:
# coordinates[0] = 99  # TypeError: 'tuple' object does not support item assignment

# Tuples can hold mixed types, just like lists
person = ("Shannon", 21, True)
print(person)

# A tuple with one item needs a trailing comma, or Python thinks it's just parentheses
not_a_tuple = (5)
actually_a_tuple = (5,)
print(type(not_a_tuple))      # <class 'int'>
print(type(actually_a_tuple))  # <class 'tuple'>

# Unpacking: assign each item to its own variable in one line
name, age, is_student = person
print(name)        # Shannon
print(age)         # 21
print(is_student)  # True

# Unpacking is great for swapping variables -- no temp variable needed
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1

# Tuples are perfect for returning multiple values from a function
def get_min_max(numbers):
    return (min(numbers), max(numbers))

low, high = get_min_max([4, 1, 9, 3])
print("low:", low, " high:", high)

# namedtuple: a tuple where each position has a name (from the collections module)
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p)    # Point(x=3, y=4)
print(p.x)  # 3 -- readable AND immutable
