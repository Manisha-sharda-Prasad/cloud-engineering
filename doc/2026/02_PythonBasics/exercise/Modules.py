# ⭐️:::::: Modules  :::::::

import math
from math import ceil, floor, trunc

# 🔸 Math Module ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#ceil(),floor(),trunc(),factorial(),sqrt(), hypot()

print('------------ceil(),floor(),trunc()--------------')
print(math.ceil(3.6))   #4
print(math.floor(3.6))  #3
print(math.trunc(3.6))  #3


#ceil() - rounds the number Upwards
print('---------------------ceil()--------------------')
print(math.ceil(3.1))    #4
print(math.ceil(3.998))  #4
print(math.ceil(3.0))    #3
print(math.ceil(-5.5))   #-5


#floor() - rounds the number Downwards
print('---------------------floor()--------------------')
print(math.floor(3.1))    #3
print(math.floor(9.0))    #9
print(math.floor(9.998))  #9


#trunc() - Does not round the numbers, instead ignore digits after decimal.
print('---------------------trunc()--------------------')
print(math.trunc(3.1))    #3
print(math.trunc(9.0))    #9
print(math.trunc(9.998))  #9
print(math.trunc(3.998))  #3


#factorial() - Multiplication of all positive integers less or equal to given number.
print('--------------------factorial()-------------------')
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))


#sqrt() - returns Square root of given no in float.
print('--------------------sqrt()-------------------')
print(math.sqrt(3))      #1.7320508075688772
print(math.sqrt(4))      #2.0
print(math.sqrt(9))      #3.0
print(math.sqrt(16))     #4.0
print(math.sqrt(100))    #10.0


#hypot() - Hypotenuse to find the longest side, if you have right-angle triangle and know lengths of 2 shortest sides.
print('--------------------hypot()-------------------')
print(math.hypot(6,8))                  #10.0

print(math.hypot(9,11))                 #14.212670403551895
print(math.hypot(9,11).__ceil__())      #15

print(math.hypot(3,4))                  #5.0
print(math.hypot(3,4).__floor__())      #5

print(math.hypot(5,6))                  #7.810249675906654
print(math.hypot(5,6).__trunc__())      #7

print(math.hypot(5,7))                  #8.602325267042627
print(math.hypot(5,7).__trunc__())      #8
