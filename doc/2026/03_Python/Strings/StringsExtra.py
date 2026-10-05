#Basic strings:

#🔸len,index,backlash:
#len:
print('-----------------len,index,backlash,--------------------')
print(len('hi there!'))
print(len(''))
#index:
print('hi there!'[0])
print('hi there!'[1:])
#backlash \: info for python to know the char coming after backlash is a special char
print('I\'m Mani')

#🔸ASCII/ Code point : each char has a certain no. assigned to it.
print('-----------------ASCII/Code-point--------------------')
# ord:
print(ord('a'))
print(ord('@'))
print(ord('A'))
print(ord(' '))
print(ord('\''))
print(ord('.'))

# chr:
print(chr(98))
print(chr(100000))
#print(chr(100000111))   #ValueError: chr() arg not in range(0x110000)

#🔸Multi-line strings:
print('-----------------Multi-line-strings--------------------')
multi_line = '''line1

line2'''
print(len(multi_line))              #counts empty space too


#🔸Searching inside Strings:
print('-----------------Searching-in-strings--------------------')
#strings.index
print('ILoveMyself'.index('M'))

