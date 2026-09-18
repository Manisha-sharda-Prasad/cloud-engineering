#Data Structures: Lists Fundamentals, List Advanced, Other DS
import copy


#🔸Lists Fundamentals :
# Create, Access & Read, Unpack, Explore & Analyze, Change, Order, Copy, Test, Combine, Iterate, Filter, Transform


#▪️Create Lists[] ::::::::::::::::::::::::::::::::::::::::::
#Lists, Nested Lists - Matrix

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




#▪️Access & Read :::::::::::::::::::::::::::::::::::::::::::
#Indexing[], Nested Lists(Matrix), slicing()

#Indexing️[] -(Get Single item)
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




#▪️Unpack - ::::::::::::::::::::::::::::::::::::::::::
# Lists[], Asterisk*, underscore "_"
# Unpacking Rules:
# 1.Num of Var == match Num of the values - not less, more
# 2.Asterisk collects leftovers, fine if there are none
# 3.Use '*' or '*_' using multiple'_,_,_' takes time

#lists[]
print("-----------------Unpack-:-lists[]-----------------------")
person = ["Manisha", 30, "Fashion Stylist", "USA"]
name, age, role, country = person              #order of variables should be right
print(name, age)

#Rest Collector -Asterisk * : (first, *rest , last)
print("------------Unpack-:-Rest-Collector-Asterisk*-----------")
namee, *details, place = person
print(namee, type(details))
print(details)        #Collected Unnecessary stuff using '*'
print(place)

*rest, places = person      #one *asterisk at one time
print(rest)
print(places)

# unpacking and skipping with underscore "_" : (not assigning unnecessary vars)
print("---------------Unpack-:-Underscore'_'--------------------")
info = ["Lekh", 30, "Stylist", "123", "New York"]
user, _, ids, _, _ = info
print(user, ids)

fullname, *_ = info
*_, state = info
print(fullname)
print(state)



#▪️Explore & Analyze ::::::::::::::::::::::::::::::::::::::::::
# max,min,sum,len,all,any,count,index,operators

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


print("------------Check-&-Analyze-:-Operators(==,>,<,is)--------------")
onn = [1, 3, 4, 6, 8]
print(nums == onn)
print(nums < onn)
print(nums is onn)    #both pointing at same data? no-false




#▪️Change Lists[] ::::::::::::::::::::::::::::::::::::::::::
#Change lists: Append, Insert, Remove, Clear, Pop, Update

print("----------Change-:-Append,Insert,Remove,Clear,Pop,Update-----------")
alpha = ['a','b','c','d']

alpha.append('E')
alpha.append('F')
print("Append : ",alpha)

alpha.insert(0,'X')
alpha.insert(1,'Y')
print("Insert : ",alpha)

alpha.remove('Y')
alpha.remove('X')
print("Remove : ",alpha)

alpha.pop(-1)
alpha.pop()
print("Pop : ",alpha)

removed = alpha.pop()
print("Removed Item(pop):", removed)
print(alpha)

alpha[0],alpha[1] = 'A', 'B'
print("Update : ",alpha)

alpha.clear()
print("Clear : ",alpha)



#▪️Order Lists[] ::::::::::::::::::::::::::::::::::::::::::
#Sort, Reverse=, Sorted, Reverse(), Reversed

print("----------Order-:-Sort,Reverse=,Sorted,Reverse(),Reversed-----------")
letter = ['c','d','a','b']

let_matrix = [
    ['c','d','a','b'],
    ['a','b','c','d'],
    ['x','u','v','w']
]

letter.sort()                                           #'sort()' -ascending (low-high), doesnt return
print("Sort: ",letter)

let_matrix.sort()    # n = sorted(let_matrix)           #sort 'first' item of every[[0,][0,]] in matrix lists[]
print("Sort: ",let_matrix)

letter.sort(reverse= True)                              #sort with 'reverse=True'- 'descending' (high-low)
print("Reverse Sort: ",letter)

let_matrix.sort(reverse= True)
print("Reverse Sort: ",let_matrix)

new_letter = sorted(letter)                             #returns 'Sorted()' new[] without changing original[]
print("Sorted: ", new_letter)

new_letter.reverse()                                    #'Reverse()'- Flips list- doesnt return
print("Reverse(): ", new_letter)

new_let_matrix = reversed(let_matrix)           #'Reversed()'- Returns new reversed []
print("Reversed original[]: ", let_matrix)
print("Reversed new[]: ", new_let_matrix)



#▪️Copy Lists[] ::::::::::::::::::::::::::::::::::::::::::
# Copy=, Shallow-Copy(), DeepCopy(),Copy.copy(),
print("----------Copy-:-Copy=,ShallowCopy,DeepCopy,Copy.copy-----------")
data =  ['x','u','v','w'] # "data" is object created from class "List" | type(data) == List class

copy_data = data                                         #Risky copy/assigning data by '=' , but changes 'original[]'
print(data)
print("Copy=: ",copy_data)

copy_new_data = copy.copy(data)                          #Shallow 'copy.copy()' for simple lists ('import copy' module)
print("Shallow Copy: ",copy_new_data)


copy_new_data = copy.deepcopy(data)                      #'Deepcopy' for nested lists ('import copy' module)
data.pop()
data.append('K')
data.insert(0,'P')
print("Original data[]: ",data)
print("Deep Copy: ",copy_new_data)                      #Doesn't affect the copy as used - '.deepcopy()'



#▪️Test Lists[] ::::::::::::::::::::::::::::::::::::::::::
#Is =
print("--------------------Test-:-Is=--------------------")

copy_new_data = data
print("Is=: ",data is copy_new_data)                    #Referencing to the same [] ? True

copy2 = data.copy()                                     #'copy()'
print("Is copy: ",data is copy2)



#▪️Combine Lists[] ::::::::::::::::::::::::::::::::::::::::::
# (+),(*),(,), extend(),zip()
print("--------------------Combine-:- (+),(*),(,),Extend,Zip,--------------------")

mon = ['O', 'P', 'Q', 'R']
onn = [1, 2, 3, 4, 5]

combine = mon + onn                                   # '+' [ [][] ] - Simple combine
print(combine)
print( "Multiplier * : ", mon * 2)                    # *

combine2 = [mon, onn]                                 # ',' [ [],[] ] - Nested lists,
print(combine2)

mon.extend(onn)                                       #'.extend()' - extending[ , ] by another without creating new[]
print("Extend : ",mon)
print("Extend : ",onn)


combine3 = list(zip(mon, onn))               #'Zip()' assigns each[0] with other [0] in lists tuple[(0,0), (1,1)]
print("Zip : ",combine3)




#▪️ Iterate Lists[] ::::::::::::::::::::::::::::::::::::::::::
# Enumerate,Reverse,Zip,Map
print("--------------------Iterate-:-Enumerate,Reverse,Zip,Map--------------------")

let = ['c','d','a','b','','/']
nr = [1, 3, 4, 6, 8]
new_let =[]

for l in let:
    new_let.append(l.upper())
    print("Iterate : ",new_let)

#print(enumerate(let))
print("Enumerate : ",list(enumerate(let)))      #assigns index (0, 'c'), (1, 'd')
print("Enumerate : ",list(enumerate(let, start= 1)))
#better way
for index, value in enumerate(let, start= 1):
    print("Enumerate for: ",index, value)


print("Reversed : ",list(reversed(let)))
#better way
for l in reversed(let):
    print("Reversed for: ",l)


print("Zip : ",list(zip(let, nr)))
#better way
for l, n in zip(let,nr):
    print("Zip for: ", l, n)

