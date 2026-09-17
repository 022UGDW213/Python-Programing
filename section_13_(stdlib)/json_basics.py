# Standard library tour, part 4: json (Python <-> JSON)

# JSON is the language APIs speak. Python's json module translates both ways.
import json

# Python dict -> JSON string (for sending to an API)
data = {
    "name": "amy",
    "age": 30,
    "skills": ["python", "apis"],
    "active": True,
}
json_string = json.dumps(data, indent=2)
print(json_string)
print(type(json_string))  # <class 'str'>

# JSON string -> Python dict (for using an API response)
parsed = json.loads(json_string)
print(parsed["name"])    # amy
print(parsed["skills"])  # ['python', 'apis']

# Write JSON to a file
with open("user.json", "w") as f:
    json.dump(data, f, indent=2)

# Read it back
with open("user.json") as f:
    loaded = json.load(f)
print(loaded == data)  # True

# Watch out: JSON keys are always strings, and it only supports
# str, int, float, bool, None, list, and dict.
# (datetime objects, sets, etc. need converting first.)

# Practical example: a tiny settings file
settings = {"theme": "dark", "volume": 80, "notifications": True}
with open("settings.json", "w") as f:
    json.dump(settings, f)

with open("settings.json") as f:
    print("Loaded settings:", json.load(f))

import os
os.remove("user.json")
os.remove("settings.json")  # clean up
