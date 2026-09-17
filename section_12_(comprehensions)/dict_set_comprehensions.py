# Dict and set comprehensions: same idea, different brackets

# Dict comprehension: {key: value for item in iterable}
names = ["amy", "ben", "cara"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'amy': 3, 'ben': 3, 'cara': 4}

# Build a lookup table from a list of records
users = [
    {"id": 1, "name": "amy"},
    {"id": 2, "name": "ben"},
    {"id": 3, "name": "cara"},
]
users_by_id = {user["id"]: user["name"] for user in users}
print(users_by_id)  # {1: 'amy', 2: 'ben', 3: 'cara'}

# Flip a dictionary (keys become values and vice versa)
flipped = {name: uid for uid, name in users_by_id.items()}
print(flipped)

# With a condition: only keep passing students
scores = {"amy": 92, "ben": 58, "cara": 77, "dan": 41}
passing = {name: score for name, score in scores.items() if score >= 60}
print(passing)

# Set comprehension: {expression for item in iterable}
# (looks like a dict comprehension, but there's no colon)
word = "mississippi"
unique_letters = {letter for letter in word}
print(unique_letters)

# Practical: unique domains from a list of emails
emails = ["amy@example.com", "ben@test.org", "cara@example.com"]
domains = {email.split("@")[1] for email in emails}
print(domains)  # {'example.com', 'test.org'}

# Quick reference:
#   [ ... ]  -> list comprehension
#   {k: v ...} -> dict comprehension (has a colon)
#   { ... }  -> set comprehension (no colon)
