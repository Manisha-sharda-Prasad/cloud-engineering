# ⭐️:::::: Modules  :::::::

# 🔸 Math Module ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
import math

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
print('---------------------sqrt()--------------------')
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



# 🔸 Random Module ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
import random
#random(), seed(), choice()

#random()- prints random number each time
print('-----------------random()----------------------')
print(random.random())
print(random.random())
print(random.random())

#seed() - starts from '0.'
print('-----------------seed()----------------------')
random.seed(0)
print(random.random())
print(random.random())
print(random.random())

#choice() - chooses random item from given choice of [] and can repeat the same item.
print('-----------------choice()----------------------')
nums = [1,2,3,4,5,6,7,8,9,10]
names = ["Nashi","Rashi","Phi","Nhi"]

print(random.choice(nums))
print(random.choice(nums))

print(random.choice(names))
print(random.choice(names))


#sample() - randomly selects the given unique items (unique indexes), doesn't verify whether items at these indexes are unique.
print('-----------------sample()----------------------')
name = ["Nashi","Rashi","Phi","Nhi"]

print(random.sample(name, 3))                        #returns list[] with 3 items
print(random.sample(name, 3))
print(random.sample(name, 4))
print(random.sample(name, 4))
#print(random.sample(name, 5))                          #throws error as items are not 5




# 🔸 Platform Module ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
import platform
#platform(),machine(), processor(), system(), python_implementation(), python_version(), python_version_tuple()

#platform() - shows platform from where we are
print('-----------------Platform-Module-------------------')

print(platform.platform())                              #macOS-15.7.7-arm64-arm-64bit-Mach-O
print(platform.platform(True, True))       #macOS-15.7.7

#machine() - returns generic name of the processor runs OS.
print(platform.machine())                               #arm64

#processor() - returns real name of processor
print(platform.processor())                             #arm

#system() - returns generic name of OS name             #Darwin
print(platform.system())

#python_implementation() - returns name of your Python Implementation(written in C language)
print(platform.python_implementation())                 #CPython

#python_version() - returns puthon version
print(platform.python_version())                        #3.13.5

#python_version_tuple() - does not return any string unlike others(), instead Py version as 'Tuple' with 3 items
print(platform.python_version_tuple())                  #('3', '13', '5') - 3.13.5

