# ::::: Numeric Types : Math Operators, Rounding :::::
import math
from math import floor, ceil, trunc
from random import random

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


#🔸Math Operators: ---> + , - , * , / , // , % , ** , = , += , -=, *= ---------------------------
# / , // , % , **
print(7 / 2)
print(7 // 2)                               #removes .0
print(7 % 2)                                #remainder 1
print(7 ** 2)                               # 7*7

# =, +=, -=, *=
o = 3
o += 3                                      # o = o + 3 (3+3=6)
print(o)

o -= 1                                      # o = o - 1 (6-1=5)
print(o)

o *= 2                                      # o = o * 2 (5*2=10)
print(o)


#🔸Rounding: ---> abs(), round(), ceil(), floor(), trunc() ---------------------------
#abs()
print(2 - 10)           #-8
print(abs(2 - 10))      # 8

#round()                                      # rounds float at top (round(): handy in data analysis/saves space)
price = 34.957564
print(round(price))
print(round(price,3))                         # .000 need '3'

#floor()                                      # rounds float at bottom
import math
print(floor(price))
#print(math.floor(price))                     # or

#ceil()                                       # rounds float at top (ceil(): data engineering/splitting data in batches)
print(ceil(price))
#print(math.ceil(price))

#trunc()
print(trunc(price))                           # removes decimal, whole number remains same(no rounding)
#print(int(price))                            # or


#🔸Random: ---> random(), randint()  ---------------------------
#random()                                       #return float 0.0 and 1.0/ fake data fill
import random
print(random.random())


#randint()                                       # test data(dummy) - age,ID,price
print(random.randint(1,6))

numb = random.randint(1, 100)
print(numb)
checkEven = (numb % 2 == 0)
print(checkEven)



#🔸Validation: ---> is_integer(), isinstance()  ---------------------------
#is_integer()                                    #checks float .0(can be whole int) or .1(float)...
m = 7.0
n = 7.1
print(m.is_integer())
print(n.is_integer())

#isinstance()
print(isinstance(m, int))                       # False/ m = 7.0
print(isinstance(m, float))                     # True




#🔸Advances Math: ---> sqrt(), sin(), cos(), log()  ---------------------------

