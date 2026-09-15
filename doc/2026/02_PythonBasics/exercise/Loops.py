# :::::  Loops  ::::::

# For Loop, While Loop

# 🔸'For Loop': Go through values and aggregate data - summing, counting, averaging:
# ▪️break, continue, pass
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
numb = 7
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


# ▪️break::: stop immediately- critical problems
print("-------- break --------")
names = ["Raj","Vir","Rey","","Ian",""]
for n in names:
    if n == "":
        print("'' Detected")
        break
    print(f"{n}")

# break: use it with 'else' statement
print("-------- break-else--------")
items = [1,5,3,2,9,4]
for i in items:
    if i % 2 == 0:
        print("Even number found")
        break
else:
    print("All numbers are Odd")



# ▪️continue::: skip iteration - noncritical
print("-------- continue --------")
for n in names:
    if n == "":
        print("Unknown")
        continue
    print(f"{n}")


# ▪️pass::: Do nothing
print("-------- pass --------")
for n in names:
    if n == "":
        pass                      #e.g. later: you can use n = n.replace("", unknown)
    print(f"Name = {n}")

