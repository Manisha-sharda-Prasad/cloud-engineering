# ⭐️:::::: Modules  :::::::

import math
from math import ceil, floor, trunc

# 🔸 Math Module ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#ceil(),floor(),trunc()
print('-----------ceil(),floor(),trunc()--------------')
print(math.ceil(3.6))   #4
print(math.floor(3.6))  #3
print(math.trunc(3.6))  #3


#ceil() - rounds the number Upwards
print('-----------------------ceil()--------------------')
print(math.ceil(3.1))    #4
print(math.ceil(3.998))  #4
print(math.ceil(3.0))    #3
print(math.ceil(-5.5))   #-5


#floor() - rounds the number Downwards
print('-----------------------floor()--------------------')
print(math.floor(3.1))    #3
print(math.floor(9.0))    #9
print(math.floor(9.998))  #9


#trunc() - Does not round the numbers, instead ignore digits after decimal.
print('-----------------------trunc()--------------------')
print(math.trunc(3.1))    #3
print(math.trunc(9.0))    #9
print(math.trunc(9.998))  #9
print(math.trunc(3.998))  #3

