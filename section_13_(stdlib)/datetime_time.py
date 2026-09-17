# Standard library tour, part 1: datetime and time

# Python ships with "batteries included" -- useful modules you don't have to install.
# You just import them.

from datetime import datetime, date, timedelta

now = datetime.now()
print(now)                    # 2026-09-17 01:23:45.123456
print(now.year, now.month, now.day)
print(now.strftime("%A, %B %d, %Y"))  # Thursday, September 17, 2026

# Parse a string into a datetime
birthday = datetime.strptime("1990-05-21", "%Y-%m-%d")
print(birthday)

# Date math with timedelta
today = date.today()
next_week = today + timedelta(days=7)
print("Today:", today)
print("Next week:", next_week)
print("Days apart:", (next_week - today).days)

# How old is something, in days?
launch = date(2026, 1, 1)
print("Days since launch:", (today - launch).days)

# The time module: measuring how long code takes
import time

start = time.time()
total = sum(range(1000000))
elapsed = time.time() - start
print(f"Summed a million numbers in {elapsed:.4f} seconds")

# Pause your program
print("Waiting 1 second...")
time.sleep(1)
print("Done!")

# Quick reference for strftime codes:
#   %Y year (2026)   %m month (09)   %d day (17)
#   %H hour (24h)    %M minute       %S second
#   %A weekday name  %B month name
