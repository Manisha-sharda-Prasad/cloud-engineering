# Run with this: python3 doc/2026/02_python/exercise/exercise-00.py

data = [60, 64, 34, 25, 12, 22, 11]

# Looping with Conditions (if)
for d in data:
    if d >= 34:
        print(f"Greater or Equal to '34':{d}")   # 64 34 90

# Looping Even Numbers
for d in data:
    if d % 2 == 0:
        print(d)

# Looping with range()
for num in range(7,10):
    print(f"Count: {num}")


# Compare Every Pair - (adjacent comparison)
letters = ["A", "B", "C"]
for r in range (len(letters)):             # 'list' object '(letters)' cannot be interpreted as an integer
    for s in range (r + 1, len(letters)):
        print(f"Comparing {[r]} with {[s]}")