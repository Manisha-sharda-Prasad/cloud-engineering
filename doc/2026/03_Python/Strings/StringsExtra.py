#Basic strings:

#🔸len,index,backlash:
print('-----------------len,index,backlash--------------------')
#len:
print(len('hi there!'))
print(len(''))

#index:
print('hi there!'[0])
print('hi there!'[1:])

#backlash \: info for python to know the char coming after backlash is a special char
print('I\'m Mani')
print(len('\'\\') - len('\n'))


#🔸ASCII/ Code Point : each char has a certain no. assigned to it. Char encoding standard.
print('-----------------ASCII/Code-point--------------------')
# ord:
print('----------ord--------')
print(ord('a'))
print(ord('d'))
print(ord('@'))
print(ord('A'))
print(ord(' '))
print(ord('\''))
print(ord('.'))
print(ord('d') - ord('a'))


# chr:
print('----------chr--------')
print(chr(98))
print(chr(100000))
#print(chr(100000111))   #ValueError: chr() arg not in range(0x110000)
print(chr(ord('a')))


#🔸Multi-line strings:
print('-----------------Multi-line-strings--------------------')
multi_line = '''line1

line2'''
print(len(multi_line))              #counts empty space too


#🔸Searching inside Strings:
print('-----------------Searching-in-strings--------------------')

#index()
print('ILoveMyself'.index('M'))

#find()
print('----------find--------')
greater = 'I Love Myself The Most'
print(greater.find('are'))         #-1
print(greater.find('Lov'))         #2
print(greater.find('Lov '))        #-1
print(greater.find('The', 10))     #14
print(greater.find('The', 14))     #14
print(greater.find('Love', 2, 6))  #2

#rfind()
print('----------rfind--------')
print(greater.rfind('The'))        #-1
print(greater.rfind('Mys'))        #7
print('work work work'.rfind('work', 0, 5))

#isalnum() : returns boolean, if num-&-string
print('----------isalnum--------')
print('Mani'.isalnum())         #True
print('mani30'.isalnum())       #T
print('Mani_30'.isalnum())      #F

#isalpha(), isdigit()
print('----------isalpha,isdigit-------')
print('mani'.isalpha())
print('Mani2'.isdigit())

#islower(), issupper(), isspace(), join(), split(), sorted(), sort(), min() max()
print('----------min,max-------')
print(min('watashiwaadoriandesu'))
print(max('watashiwaadoriandesu'))


#🔸Comparing Strings:
print('-----------------Comparing-Strings--------------------')
# uppercase letters have lower numerical values than lowercase letters,  ord('P') is 80 and ord('p') is 112.
greater = 'Py' > 'py'
print(greater)                #False: 80 is smaller than 112

great = 'Python' > 'Z'
print(great)                  #False: Z bigger than P

equal = 'Python' == 'Python'
print(equal)

less = '8' < '20'
print(less)                   #False: 8 is greater than 2 (0 index)

print('Python' > 'W')

print('30' > '7')
#print('30' > 7)
