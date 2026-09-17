#Data Structures: Lists Fundamentals, List Advanced, Other DS

#🔸Lists Fundamentals : Create Lists, Access & Read, Unpacking , Explore & Analyze, Change, Soring

#▪️Create Lists[] - Lists, Nested Lists - Matrix:::::::::

#Create lists
print("-------------------Create-:-Lists[]---------------------")
empty = list()
print(empty)

letters = list('Python')               #converting each letter into 'list' items
print(letters)

numbers = list(range(5))                #printing range
print(numbers)

#Nested Lists - Matrix
print("--------------Create-:-Nested-Lists-Matrix---------------")
mat = [[1,2,3,4],
      [5,6,7,8]]
print(mat)

mixed_mat = [['a', 'b', 'c', 'd'],
             [5,6,7,8]]
print(mixed_mat)
print(type(mixed_mat))



#▪️Access & Read - indexing[], Nested Lists(Matrix), slicing():::::::::::::

#indexing️[] -(Get Single item)
print("--------------Access-&-Read-:-Indexing[]-------------------")
lsts = ['a','b','c','d']
print(lsts[0], lsts[-1])

#Nested Lists(Matrix) -(Rows of [items])
print("------------Access-&-Read-:-Nested-Lists-Matrix------------")
matrix = [
            ['a','b','c','d'],
            ['e','f','g','h'],
            ['i','j','k','l']
]
print(matrix[-1])
print(matrix[-1][-1])
print(matrix[0][2])

#Slicing [start:end] -(Get Multiple items)
print("-----------Access-&-Read-:-Slicing-[start:end]-------------")
print(matrix[:])        #printing all
print(matrix[0:2])      #index [[0],[2]]
print(matrix[-1][:2])   #targeting [[],[], ['i','j']]



#▪️Unpacking - Unpacking Rules, lists[], Asterisk*, underscore "_" :::::::::::
# Unpacking Rules
# 1.Num of Var == match Num of the values - not less, more
# 2.Asterisk collects leftovers, fine if there are none
# 3.Use '*' or '*_' using multiple'_,_,_' takes time


#lists[]
print("-----------------Unpacking-:-lists[]-----------------------")
person = ["Manisha", 30, "Fashion Stylist", "USA"]
name, age, role, country = person              #order of variables should be right
print(name, age)

#Rest Collector -Asterisk * : (first, *rest , last)
print("------------Unpacking-:-Rest-Collector-Asterisk*-----------")
namee, *details, place = person
print(namee)
print(details)        #Collected Unnecessary stuff using '*'
print(place)

*rest, places = person      #one *asterisk at one time
print(rest)
print(places)

# unpacking and skipping with underscore "_" : (not assigning unnecessary vars)
print("---------------Unpacking-:-Underscore'_'--------------------")
info = ["Lekh", 30, "Stylist", "123", "New York"]
user, _, ids, _, _ = info
print(user, ids)

fullname, *_ = info
*_, state = info
print(fullname)
print(state)


#▪️Explore & Analyze :::::::::::::::
# max,min,sum,len,all,any,count,index

print("---------------Explore-&-Analyze-:-max,min,sum,len------------")
nums =[1,3,4,6,8]

print("Max : ", max(nums))
print("Min : ", min(nums))
print("Sum : ", sum(nums))
print("Length : ", len(nums))

print("--------------Explore-&-Analyze-:-all,any,count---------------")
print("All : ", all(nums))
print("All : ", all([1,0,2]))
print("Any : ", any(nums))
print("Any : ", any([1,None,3]))
print("Any : ", any([0,None,0]))

print("--------------Explore-&-Analyze-:-count,index-----------------")
print("Count : ", nums.count(5))
print("index : ", nums.index(4))

