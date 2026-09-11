# ::::: Logic & Operators ::::::
from pyspark.sql.functions import char

# Control Flow : Boolean Expressions, Control Flow Statements  :

#🔸1.Boolean Expressions:
# ▪️Values: True, False,
# ▪️Functions: bool(), any(), all(), isinstance(),
# ▪️Comparison Operators: ==, !=, <, >, >=, <=,
# ▪️Logical Operators: and, or, not,
# ▪️Membership Operators: in, not in,
# ▪️Identity Operators: is, and !not/ is not.

#bool()
print("----------bool----------")
print(type(True))                           #<class 'bool'>
print(bool(123))
print(bool("yes"))
print(bool(0))
print(bool(""))
print(bool(None))


#any()
print("-----------any-------------")
# (0/False/ "A") any()  : need 'any' to be True
email = "p256@gmail.com"
phone = ""
name = "Manny"
print(any([email, phone, name]))          #True


#all()                                      (1/ True/ "A") all()  : need 'all' to be True)
print("-----------all-------------")
print(all([email, phone, name]))          #False

#isinstance()
print("--------isinstance---------")
print(isinstance(email, bool))
print(isinstance(name, int))

#and, or
print("----------and-or-----------")
print(4 > 2 and 7 < 3)
print(4 > 2 or 2 < 3)


# 1st priority - 'and' [True 'and' False (8 > 4 and 6 < 4) = False]
# 2nd priority - 'or' [True (5 == 5 ) = True]
# Final Result - 'or' [True 'or' False = True]
print(5 == 5 or 8 > 4 and 6 < 4)


# 1st priority - '()' [True or True (5 == 5 or 8 > 4) = True]
# 2nd priority - 'and' [False (6 < 4) = False]
#Final Result  - 'and' [True 'and' False = False ]
print((5 == 5 or 8 > 4) and 6 < 4)


# or
print("------------or------------")
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)

# not
print("-----------not------------")
print(not cpu_usage > 90)
print(not False)
print(not not False)
print(not 0)


#in
print("-----------in ------------")
user = "Manisha Prasad"
print("Prasad" in user)
print("ma" in user)                 #False - lowercase
print("Ma" in user)                 #True


#notin
print("----------not-in ------------")
print("ma" not in user)              #True - flips answer
print("Ma" not in user)              #False


#is
print("-----------is ------------")
x = ['c','b','a']
#y = ['c','b','a']
y = x                               #assigning one 'variable' to the same 'object[]'
print(x == y)
print( x is y)


#!not is not
print("-----------!not-is not ------------")
#roll_number = ""
roll_number = None
print(roll_number != "")

#print(roll_number != None and roll_number != "")
#print(roll_number != None or roll_number != "")

print(roll_number is not None and roll_number != "")
print(roll_number is not None or roll_number != "")


#: : : FUN CHALLENGE : : :
print(":::: : : FUN CHALLENGE : : ::::")

username = ""
age = "18"
email = "manycon@gmail.com"
password = "appy pie"
userOne = "Admin"
userTwo = "Moderator"
adminUser = "Verified email"
moderatorUser = "Banned"

#1.check username is not empty, and age is greater or equal to 18
print(username != "" and age >= "18")

#2.Check password is 8 characters long and doest not contain space
print((len(password) >= 8 )and " " in password)

#3.check user's email is not empty, contains '@', and ends with '.com'
print((email != "" and "@" in email) and email.endswith(".com"))

#4.check username is string, is not None, and is longer than 5 characters.
print(isinstance(username, str) and username is not None and len(username) > int(5))

#5.check user is 'admin' or 'moderator', and either they're 'banned' or 'verified email'
print((userOne == "Admin" or "Moderator") and adminUser == "Banned" or "Verified email")
print((userTwo == "Admin" or "Moderator") and moderatorUser == "Verified email" or "Banned")





#🔸2.Control Flow Statements:
# ▪️if, else, elif,
# ▪️for, while, break, continue, and pass.