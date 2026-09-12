# :::::  Conditional Statements  ::::::
import email
from unittest import case

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


#Better Way
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

grade = "A" if marks >= 90 else "B" if marks >= 80 else "F"
print(grade)



# Match case
print("'--------Match Case--------'")
country = "India"

if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
else:
    print("Unknown Country")

#Better Way
match country:
    case "United States" | "USA":
        print("US")
    case "Egypt":
        print("EG")
    case _:
        print("Unknown")



#: : : FUN CHALLENGE : : :
print(":::: : : : FUN CHALLENGE : : : ::::")

# Validate the quality and correctness of email values :
# - Must not be empty| contain'.' and '@'|at-least one @ symbol| ends with'.com','.org' or '.net'|not 254 characters longer| ends with letter or digit.|

#Note: Instead of Elif you can add multiple IFs,it will print all the conditions.
email = "manny123py@.com"

if email == "":
    print("Email cannot be empty")
elif  not (" " and "." and "@" in email):
    print("Email must contain : '', '.','@'")
elif email.endswith((".com " or ".org" or ".net")):
    print("Email must contains : '.com', '.org','.net'")
elif email.count("@") > 1:
    print("Use only one @")
elif len(email) > 254:
    print("Characters are longer than 254")
elif not email[0].isalnum() and email [-1].isalnum():
    print("Must Start and End with Letter or Digit")
else:
    print("Valid Email")




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


