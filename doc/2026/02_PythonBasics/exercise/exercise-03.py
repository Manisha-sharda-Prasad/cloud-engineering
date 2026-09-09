# :::::Strings Functions/ Methods:::::

#🔸Convert Datatypes: Types() ---> type(), str()---------------------------
#type()
text = "Hello"
numb = 20

print(type(text))
print(type(numb))

#str()
print("Your number is: " + str(numb))           #Converts to string

#Methods are Functions, belong to object/classes : value.method_name()
#.upper()
print(text.upper())                             #Method of <class str>

#.bit_length()
print(numb.bit_length())                        #Method of <class int>

numb = str(numb)                                #Converts 'numb' to str()
print(type(numb))                               #Now type() shows 'str'


#🔸Measure/Calculations: Math ---> len(), count()---------------------------
#len()
print(len(text))                                #'5'

password = "  1238pas"                          #len() counts spaces too
print(len(password))
if len(password) < 10:
    print("Your Password is too short!")

#count()
statement = """
Python is easy.
Python is powerful.
I love python.
"""
print(statement.count("Python"))             #count() - repeating times?,
print(statement.count("Py-thon"))            #count() not considering lowercase/typo




#🔸Transformations /Modify---> upper(), lower(), strip(), replace(), '+', f-string, split(), '*', '[0]', '[start:end]', '[start:end:step]'---------------------------

#upper(), lower()
print(password.upper())
print(password.lower())

#strip()
print(password.split())                     # Removes "  " whitespace

#replace()
price = "500,200"
print(price.replace(",", "."))               #500.200

#print this:: +1655/5667/45
phone = "+1655-5667-45"
print(phone.replace("-", "/"))
print(phone.replace("/", "").replace("+1", "")) #prints old format '655-5667-45'

#print this:: 491761234567
phoneNo = "+49 (176) 123-4567"
print(phoneNo.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace(" ", "").replace(" ", "").replace("-", ""))

#print this:: Name: Manisha |  Role: Data Engineer | Age:27
information = "800-Manisha, ( D@t@ Engineer ) ;; 27y  "
print(information.replace("800-", "Name: ").replace(",", " | ").replace("(", "Role:").replace("D@t@ Engineer", "Data Engineer").replace(") ;;", "|").replace("27", "Age:").replace("y  ", "27"))


#Concatenation '+'
name = "Manu"
full_name = "Prasad"
full_name = name + " " + full_name
print(full_name)

#f{}  / format{}
age = 55
print(f"My name is {full_name}, I am {age} years old. My phone number is : {phone}.")
print(f"{{Hey my age is {age} and yours?}}")

#split()
value_is = "Manu-89-USA"
print(value_is.split("-"))                  #split() - separates values

#Repeat/ multiply'*'
print("=" * 30)

#Index & Slicing with Extraction [ ], [ : ], [ : : ]
word = "Python"                            #[0,1,2,3,4,5] or [-6,-5,-4,-3,-2,-1]

#Extract first character - '[0]'
print(word[0])
print(word[-6])

#Extract [start:end] - '[0:4]'
print(word[0:4])
print(word[-6:-2])
print(word[0:-2])

#Extract [start:end:step] - '[0:3:2]'
print(word[1: :2])
print(word[-5: :2])
print(word[-5:-1:2])

reverse_string = "Lekhraj Dinkar"
print(reverse_string[: :-1])



#🔸Cleaning/Conversion (white spaces)---> lsript(), rstrip(), strip(), upper(), lower()---------------------------
#lstrip()
field = "    Engineering".lstrip()
print(field)

#rstrip()
field = "Engineering    ".rstrip()
print(field)

#strip()
field = "   Engineering   ".strip()
print(field)

field = "###Engineering###".strip("#")
print(field)

field = "   Engineering"
print(len(field))
print(len(field.strip()))               #'len' after removing whitespace using 'strip()'

print(len(field) - len(field.strip()))
print(len(field) == len(field.strip()))

#lower()
search = "Email  ".lower().strip()
data = "email".lower().strip()
print(search == data)




#🔸Search---> startswith(), endswith(), find(), 'in'---------------------------
#startswith()
contact = "+1655-5667-45"
print(contact.startswith("+164"))

#endswith()
print(contact.endswith("7-45"))

#'in'
print("@" in contact)                 #False - (@ doesn't exist)

#find()
print(contact.find("7"))              #index [9]

print(contact[2:])
print(contact[1:])

print(contact.find("-"))              #index [5]
print(contact[contact.find("-")+1:])  # '5667-45'   ['find(index)' '+' print after '1:']




#🔸Validation content---> isalpha(), isnumeric()---------------------------
#isalpha() (alphabetic :checks if string has letters)
country = "USA!1]"
print(country.isalpha())            #False as '!1]'

#isnumeric())
print(country.isnumeric())          #False as 'USA!1]'
