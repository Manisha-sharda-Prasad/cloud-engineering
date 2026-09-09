# ::::: Numeric Types/ Math Operators/ Rounding :::::

#🔸Types(): ---> type(), int() , float(), complex()---------------------------
#type()
x = 5
y = 5.7
z = 2 + 3j
print(type(x),type(y),type(z))

#int()
xy = "20"
xy = int(xy)                                  #Converts 'string' to <class 'int'>
print(type(xy))
print(xy * 4)

#float()
z = 3
z = float(z)                                  #Converts 'int' to <class 'float'>
print(type(z))
print(z)

#complex()
p = 3           #real
q = 5           #imaginary
print(complex(p,q))


#🔸Math Operators(): ---> + , - , * , / , // , % , ** , = , += , -=, *= ---------------------------
# / , // , % , **
print(7 / 2)
print(7 // 2)                               #removes .0
print(7 % 2)                                #remainder 1
print(7 ** 2)                               # 7*7

# =, +=, -=, *=
o = 3

o += 3                                    # o = o + 3 (3+3=6)
print(o)

o -= 1                                    # o = o - 1 (6-1=5)
print(o)

o *= 2                                    # o = o * 2 (5*2=10)
print(o)

