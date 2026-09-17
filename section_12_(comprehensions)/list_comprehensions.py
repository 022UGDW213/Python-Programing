# List comprehensions: build lists in one readable line

# The long way
squares = []
for n in range(10):
    squares.append(n * n)
print(squares)

# The comprehension way: [expression for item in iterable]
squares = [n * n for n in range(10)]
print(squares)

# Add a condition: [expression for item in iterable if condition]
evens = [n for n in range(20) if n % 2 == 0]
print(evens)

# Transform strings
names = ["amy", "ben", "cara"]
shouted = [name.upper() for name in names]
print(shouted)

# if/else goes BEFORE the for when you're choosing between two values
labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]
print(labels)

# Nested loops: flattened in one line (reads left to right, like nested for loops)
pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
print(pairs)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Practical example: clean up messy data
raw_prices = ["$4.50", "$12.00", "free", "$7.25"]
prices = [float(p.replace("$", "")) for p in raw_prices if p.startswith("$")]
print(prices)  # [4.5, 12.0, 7.25]

# Don't overdo it: if a comprehension needs 3+ conditions or nested
# if/else, a regular loop is easier to read. Readability counts!
