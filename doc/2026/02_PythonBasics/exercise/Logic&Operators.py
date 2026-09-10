# ::::: Logic & Operators ::::::

# Control Flow : Control Flow Statements, Boolean Expressions :

#🔸1.Control Flow Statements:
# ▪️if, else, elif,
# ▪️for, while, break, continue, and pass.

















#🔸2.Boolean Expressions:
# ▪️Values: True, False,
# ▪️Functions: bool(), any(), all(), isinstance(),
# ▪️Comparison Operators: ==, !=, <, >, >=, <=,
# ▪️Logical Operators: and, or, not,
# ▪️Membership Operators: in, not in,
# ▪️Identity Operators: is, and is not.

#bool()
print(type(True))                           #<class 'bool'>
print(bool(123))
print(bool("yes"))
print(bool(0))
print(bool(""))
print(bool(None))


#any()                                      (0/False/ "A") any()  : need 'any' to be True
email = "p256@gmail.com"
phone = ""
username = "Manny"
print(any([email,phone,username]))          #True


#all()                                      (1/ True/ "A") all()  : need 'all' to be True)
print(all([email,phone,username]))          #False

#isinstance()
print(isinstance(email, bool))
print(isinstance(username, int))

#and, or
print(4 > 2 and 7 < 3)
print(4 > 2 or 2 < 3)
print("----------")

# 1st priority - 'and' [True 'and' False (8 > 4 and 6 < 4) = False]
# 2nd priority - 'or' [True (5 == 5 ) = True]
# Final Result - 'or' [True 'or' False = True]
print(5 == 5 or 8 > 4 and 6 < 4)


# 1st priority - '()' [True or True (5 == 5 or 8 > 4) = True]
# 2nd priority - 'and' [False (6 < 4) = False]
#Final Result  - 'and' [True 'and' False = False ]
print((5 == 5 or 8 > 4) and 6 < 4)


# or
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)

# not
print(not cpu_usage > 90)
print(not False)
print(not not False)
print(not 0)
