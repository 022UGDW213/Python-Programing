# Tuples vs Lists: which one should you use?

# Rule of thumb:
#   - List: a collection of similar things that might change (shopping cart, todo items)
#   - Tuple: a fixed group of related things that won't change (coordinates, RGB color, a database row)

# Lists change
shopping_cart = ["milk", "eggs"]
shopping_cart.append("bread")
print(shopping_cart)

# Tuples don't -- use them for records
rgb_red = (255, 0, 0)
print("Red as RGB:", rgb_red)

# Tuples can be dictionary keys; lists can't (because dict keys must be immutable)
locations = {
    (38.9, -77.0): "Washington, DC",
    (40.7, -74.0): "New York City",
}
print(locations[(38.9, -77.0)])

# This would crash:
# bad_key = {[1, 2]: "nope"}  # TypeError: unhashable type: 'list'

# Tuples are slightly faster and use less memory than lists
import sys
as_list = [1, 2, 3, 4, 5]
as_tuple = (1, 2, 3, 4, 5)
print("list bytes:", sys.getsizeof(as_list))
print("tuple bytes:", sys.getsizeof(as_tuple))

# Converting between them is easy
print(tuple(as_list))  # (1, 2, 3, 4, 5)
print(list(as_tuple))  # [1, 2, 3, 4, 5]

# Summary:
#   Need to add/remove/reorder items? -> list
#   Fixed record, dict key, function returning multiple values? -> tuple
#   Need uniqueness or set math? -> set (see sets_basics.py)
