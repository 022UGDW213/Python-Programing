# Standard library tour, part 2: os and sys (talking to your computer)

import os
import sys

# Where am I?
print(os.getcwd())

# What's in this folder?
print(os.listdir(".")[:5])  # first 5 entries

# Build file paths the right way (works on Windows, Mac, and Linux)
path = os.path.join("section_13_(stdlib)", "datetime_time.py")
print(path)
print("Exists?", os.path.exists(path))
print("Is a file?", os.path.isfile(path))

# Environment variables (like API keys -- never hardcode secrets!)
home = os.environ.get("HOME", "unknown")
print("Home directory:", home)

# sys: information about Python itself
print("Python version:", sys.version.split()[0])
print("Platform:", sys.platform)

# Command-line arguments: try running
#   python3 os_sys.py hello world
# sys.argv is always a list; argv[0] is the script name
print("Arguments:", sys.argv)
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])

# Exit with a status code (0 = success, anything else = error)
# sys.exit(0)

# Practical example: only run when executed directly (not when imported)
def main():
    print(f"Running on {sys.platform} with Python {sys.version.split()[0]}")

if __name__ == "__main__":
    main()
