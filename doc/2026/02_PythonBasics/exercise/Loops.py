# :::::  Loops  ::::::

# 🔸For Loop, While Loop

# 'For Loop': Go through values and aggregate data - summing, counting, averaging:
print('----Looping within List/sequence----')
for i in (1,2,3,4,5):
    print(f"Round: {i}")


scores = [60,30,80,50]
total = 0
print('----Looping within object----')
for score in scores:
    total += score
    print("Current Total :", total)
print("** Final Total :", total)


# right order : Clean --> Transform
files = [" Report.csv   ", "DATA.csv   ", " final.TXT"]
print("----Looping with 'strip','lower','replace'---")
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing {file}")



print("----Looping with range() and 'step'----")
for num in range(4,10,2):
    print(f"Count: {num}")


data = [60, 64, 34, 25, 12, 22, 11]
print('----Looping with Conditions (if)----')
for d in data:
    if d >= 34:
        print(f"Greater or Equal to '34':{d}")   # 64 34 90


print('----Looping with Even Numbers----')
for d in data:
    if d % 2 == 0:
        print(d)


print("-----Compare Pairs: Adjacent comparison-----")
letters = ["A", "B", "C"]
for r in range (len(letters)):             # 'list' object '(letters)' cannot be interpreted as an integer
    for s in range (r + 1, len(letters)):
        print(f"Comparing {[r]} with {[s]}")



digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numb = 7
print("-----Multiplication-----")
for d in digits:
    print(f"{numb} * {d} = ", d * numb)

#better way
print("-----Multiplication with range-----")
n = 11
m = 0
for r in range(1,n):
    m = r * numb
    print(f"{numb} * {r} = {m}")



n = 7
print("-----Nested-for-loop-(pyramid-exercise)-----")
for r in range(1,n + 1):
    for s in range(0,r):
        print("*", end="")
    print("")
