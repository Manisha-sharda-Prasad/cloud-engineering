# :::::  Conditional Statements  ::::::

# 🔸 Standalone If, Else, Elif, Nested If, Independent If, Inline if(Ternary), Match case


# if, elif, else, nested if
print('--------if-elif-else-nestedif-------')
score = 90
submitted_project = True

if score >= 60:
    if submitted_project:
        print("⭐️🎉Congratulations You Passed the Exam, You got A+ !!⭐️")
    else:
        print("⭐️ You Passed the Exam!!")
elif score >= 50:
    print("❇️ You Passed the Exam, but need more practice!")
elif score >= 40:
    print("❇️ You Passed the Exam, but need more practice!")
else:
    print("💔Better luck next time, need more practice!✍️")



marks = 100
assignment = True
if marks >= 90 and assignment is True:
    print("A+")
elif score >= 60 and assignment is not True:
    print("A")
else :
    print("F")


# Inline if(Ternary)
print('--------Inline if(Ternary)-------')

print("A" if marks >= 90 else "F")

grade = "A" if marks >= 90 else "F"
print(grade)



# Using Conditions with 'for'
data = [60, 64, 34, 25, 12, 22, 11]

print('----Looping with Conditions (if)----')
for d in data:
    if d >= 34:
        print(f"Greater or Equal to '34':{d}")   # 64 34 90


print('----Looping with Even Numbers----')
for d in data:
    if d % 2 == 0:
        print(d)


print('----Looping with range()----')
for num in range(7,10):
    print(f"Count: {num}")


print("-----Compare Pairs -Adjacent comparison-----")
letters = ["A", "B", "C"]
for r in range (len(letters)):             # 'list' object '(letters)' cannot be interpreted as an integer
    for s in range (r + 1, len(letters)):
        print(f"Comparing {[r]} with {[s]}")


