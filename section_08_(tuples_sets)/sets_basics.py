# Sets: collections with no duplicates and no order

# A set is like a list, except:
#   1. Every item appears only once (duplicates are removed automatically)
#   2. Items have no order -- you can't do my_set[0]

colors = {"red", "blue", "red", "green", "blue"}
print(colors)  # {'red', 'blue', 'green'} -- order may vary, duplicates are gone

# Adding and removing
colors.add("purple")
print(colors)

colors.remove("blue")   # crashes with KeyError if "blue" isn't there
colors.discard("blue")  # safe version -- does nothing if it's missing
print(colors)

# The fastest way to remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers))
print(unique_numbers)

# Sets are built for math-style operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # union: everything in either set -> {1, 2, 3, 4, 5, 6}
print(a & b)  # intersection: only in both -> {3, 4}
print(a - b)  # difference: in a but not in b -> {1, 2}
print(a ^ b)  # symmetric difference: in exactly one -> {1, 2, 5, 6}

# Membership tests are super fast in sets (much faster than in lists)
big_list = list(range(100000))
big_set = set(big_list)
print(99999 in big_set)   # True, and basically instant
print(99999 in big_list)  # True, but Python checks every item one by one

# Practical example: who RSVP'd but didn't show up?
rsvps = {"amy", "ben", "cara", "dan"}
attended = {"amy", "cara"}
no_shows = rsvps - attended
print("No shows:", no_shows)

# frozenset: an immutable set (like tuple is to list)
frozen = frozenset([1, 2, 3])
print(frozen)
# frozen.add(4)  # AttributeError -- can't change a frozenset
