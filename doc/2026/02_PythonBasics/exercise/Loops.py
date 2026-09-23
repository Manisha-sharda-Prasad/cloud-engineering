from itertools import count
# ⭐️ ::::: Loops  ::::::
# Loops :- For Loop, While Loop

# 🔸'For Loop': :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Go through values and aggregate data -summing,counting,Loop over 'Fixed Sequence':

# ▪️ Nested Loop, Break, Continue, Pass :

print('----Looping within List/sequence----')
for i in (1,2,3,4,5):
    print(f"Round: {i}")



print('----Looping within object----')
scores = [60,30,80,50]
total = 0
for score in scores:
    total += score
    print("Current Total :", total)
print("** Final Total :", total)


# strip(),lower(),replace
# right order : Clean --> Transform
print("----Looping with 'strip','lower','replace'---")

files = [" Report.csv   ", "DATA.csv   ", " final.TXT"]
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing {file}")



print("----Looping with range() and 'step'----")
for num in range(4,10,2):
    print(f"Count: {num}")


print('----Looping with Conditions (if)----')
data = [60, 64, 34, 25, 12, 22, 11]
for d in data:
    if d >= 34:
        print(f"Greater or Equal to '34':{d}")   # 64 34 90


print('----Looping with Even Numbers----')
for d in data:
    if d % 2 == 0:
        print(d)


# ▪️Nested Loop: (Outer - Inner forloop)
print("-----Nested-loop:--(Compare Pairs: Adjacent)-----")
for x in range(3):              #(0,1,2)
    for y in range(2):          #(0,1)
        print(f"Comparing x {[x]} with y {[y]}")


print("--------Nested-loop---------")
alphabet = ["a", "b", "c", "d"]
for x in alphabet:
    for y in alphabet:
        print(f" x{[x]} with y{[y]}")


print("-----Nested-loop-(Pyramid)-----")
n = 7
for r in range(1,n+1):
    for s in range(0,r):
        print("*", end="")
    print("")


print("-----Multiplication-----")
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numb = 7
for d in digit:
    print(f"{numb} * {d} = ", d * numb)

#better way
print("-----Multiplication with range-----")
numb = 7
n = 11
m = 0
for r in range(1,n):
    m = r * numb
    print(f"{numb} * {r} = {m}")




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


#check duplicate files
print("-------- break-else--------")

file_list = ["report.csv","data.xlsx","summary.docx","report.csv","data.csv"]
for f in file_list:
    if f * 2  or f * 3  or f * 4:
        print("Duplicate files found")
        break
else:
    print("All files are unique")


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
        pass                            #e.g. later: you can use n = n.replace("", unknown)
    print(f"Name = {n}")




# 🔸'While Loop': ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#Repeats  block of code - over and over as long as condition true

#▪️While Condition(Exists Normally)
print("-------- While Loop-Condition--------")
answer = ""
while answer != "yes":
    answer = input("Do you agree? yes/no: ")
print("Thank You")


#▪️While True(Must have extra if+break)
print("-------- While Loop-True--------")
while True:
    ans = input("Do you agree? yes/no: ")
    if ans == "yes":                    #if we are not fulfilling, python will keep asking
        break
print("Thank You")



#challenge - if '3' strikes, and not fulfilling condition print a message.
print("-------- While Loop-Else challenge--------")
strikes = 0
while strikes < 3:
    ans = input("Do you agree with me? yes/no: ").strip().lower()
    if ans == "yes":
        print("Glad we are on the same page!😊")
        break
    strikes += 1                          #input ++
else:
    print("3 strikes you are out!!🥺")


