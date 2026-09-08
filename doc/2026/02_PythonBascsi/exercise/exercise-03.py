# Run with this: python3 doc/2026/02_Python/exercise/exercise-03.py
# or Copy Path reference - content root from: pyspark.sql.functions import count

text = "Hello"
numb = 20
#Types() ---> type(), str()
print(type(text))
print(type(numb))

print("Your number is: " + str(numb))           #Converts to string

#Methods are Functions, belong to object/classes : value.method_name()
print(text.upper())                             #Method of <class str>
print(numb.bit_length())                        #Method of <class int>

numb = str(numb)                                #Converts 'numb' to str()
print(type(numb))                               #Now type() shows 'str'


#Math ---> len(), count()
print(len(text))                                #'5'

password = "  1238pas"                          #len() counts spaces too
print(len(password))
if len(password) < 10:
    print("Your Password is too short!")


statement = """
Python is easy.
Python is powerful.
I love python.
"""
print(statement.count("Python"))             #count() not considering lowercase/typo
print(statement.count("Py-thon"))








