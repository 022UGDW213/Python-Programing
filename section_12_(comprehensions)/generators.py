# Generators: lazy sequences that produce one item at a time

# A list comprehension builds the WHOLE list in memory at once.
# A generator expression builds items one at a time, only when asked.
# (Parentheses instead of square brackets.)

big = (n * n for n in range(10))
print(big)  # <generator object ...> -- nothing computed yet!

print(next(big))  # 0
print(next(big))  # 1
print(next(big))  # 4 -- values appear on demand

# They still work in loops, sum(), etc.
total = sum(n * n for n in range(1000000))
print(total)  # no giant list ever lived in memory

# yield: turn any function into a generator
def countdown(n):
    while n > 0:
        yield n   # pause here, hand n to the caller, resume on next()
        n -= 1

for number in countdown(5):
    print(number)

# Why bother? Imagine reading a 10 GB log file.
# A list would try to load all 10 GB at once. A generator reads line by line.
def error_lines(filename):
    with open(filename) as f:
        for line in f:
            if "ERROR" in line:
                yield line.strip()

# (Try it: create a small test file first)
with open("sample.log", "w") as f:
    f.write("INFO all good\nERROR disk full\nINFO still good\nERROR timeout\n")

for line in error_lines("sample.log"):
    print("Found:", line)

import os
os.remove("sample.log")  # clean up our test file

# Generators are single-use: once consumed, they're empty
g = (n for n in range(3))
print(list(g))  # [0, 1, 2]
print(list(g))  # [] -- already used up!

# Summary: list/dict/set comprehensions for small data you want to keep,
# generators (and yield) for big or endless data you want to stream.
