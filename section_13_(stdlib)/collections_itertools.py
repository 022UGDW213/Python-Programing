# Standard library tour, part 3: collections and itertools (power tools)

from collections import Counter, defaultdict, deque
import itertools

# Counter: count how many times each item appears
votes = ["amy", "ben", "amy", "cara", "amy", "ben"]
tally = Counter(votes)
print(tally)              # Counter({'amy': 3, 'ben': 2, 'cara': 1})
print(tally.most_common(2))  # [('amy', 3), ('ben', 2)]

# Counter works on strings too
print(Counter("mississippi"))

# defaultdict: a dict that auto-creates missing keys
word_lengths = defaultdict(list)  # missing keys start as []
for word in ["cat", "dog", "fish", "bird", "ant"]:
    word_lengths[len(word)].append(word)
print(dict(word_lengths))  # {3: ['cat', 'dog', 'ant'], 4: ['fish', 'bird']}

# deque: a double-ended queue -- fast appends/pops on BOTH ends
queue = deque(["first", "second"])
queue.append("last")       # add to the right
queue.appendleft("zeroth") # add to the left
print(queue)
print(queue.popleft())  # 'zeroth' -- lists are slow at this; deque is fast

# itertools: memory-efficient looping tools

# chain: loop over several iterables as one
for item in itertools.chain([1, 2], ["a", "b"], (True,)):
    print(item)

# combinations: all pairs, no repeats
print(list(itertools.combinations(["a", "b", "c"], 2)))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

# permutations: all orderings
print(list(itertools.permutations(["a", "b", "c"], 2)))

# cycle: loop forever (use with a break or zip!)
colors = itertools.cycle(["red", "green", "blue"])
for i, color in zip(range(5), colors):
    print(i, color)

# These return iterators (like generators) -- they don't build big lists.
