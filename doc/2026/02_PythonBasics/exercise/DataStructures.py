#Data Structures: Lists Fundamentals, List Advanced, Other DS

#🔸Lists Fundamentals : Create Lists, Access & Read, Unpacking , Explore & Analyze, Change, Soring

#▪️Create Lists[] - Lists, Nested Lists - Matrix:::::::::

#Create lists
print("------------------Create-Lists----------------------")
empty = list()
print(empty)

letters = list('Python')               #converting each letter into 'list' items
print(letters)

numbers = list(range(5))                #printing range
print(numbers)

#Nested Lists - Matrix
print("--------------Nested-Lists-Matrix----------------")
mat = [[1,2,3,4],
          [5,6,7,8]]
print(mat)

mixed_mat = [['a', 'b', 'c', 'd'],
             [5,6,7,8]]
print(mixed_mat)
print(type(mixed_mat))


#▪️Access & read - indexing[], Nested Lists(Matrix), slicing():::::::::::::

#indexing️[] -(Get Single item)
print("------------------Indexing[]----------------------")
lsts = ['a','b','c','d']
print(lsts[0], lsts[-1])

#Nested Lists(Matrix) -(Rows of [items])
print("-----------------Nested-Lists-Matrix--------------")
matrix = [
            ['a','b','c','d'],
            ['e','f','g','h'],
            ['i','j','k','l']
]
print(matrix[-1])
print(matrix[-1][-1])
print(matrix[0][2])

#Slicing [start:end] -(Get Multiple items)
print("-----------------Slicing-[start:end]----------------")
print(matrix[:])        #printing all
print(matrix[0:2])      #index [[0],[2]]
print(matrix[-1][:2])   #targeting [[],[], ['i','j']]



#▪️Unpacking - Unpacking Rules, lists[], Asterisk*, underscore "_"
# Unpacking Rules
# 1.Num of Var must match the values exactly - not less, more
# 2.asterisk collects leftovers, fine if there are none


#lists[]
print("-----------------Unpacking - lists[]----------------")
person = ["Manisha", 30, "Fashion Stylist", "USA"]
name, age, role, country = person              #order of variables should be right
print(name, age)

#Rest Collector -Asterisk * : (first, *rest , last)
print("--------------Rest Collector-Asterisk*-------------------")
namee, *details, place = person
print(namee)
print(details)        #Collected Unnecessary stuff using '*'
print(place)

*rest, places = person      #one *asterisk at one time
print(rest)
print(places)

# unpacking with underscore "_" : (not assigning unnecessary vars)
print("-------------Unpacking-underscore'_'-------------------")
info = ["Lekh", 30, "Stylist", "123", "New York"]
user, _, ids, _, _ = info
print(user, ids)

fullname, *_ = info
*_, state = info
print(fullname)
print(state)
