
# Lists, Access & Read

#🔸Create Lists[] - Lists, Nested Lists - Matrix,

#▪️Create lists
print("------------------Create-Lists----------------------")
empty = list()
print(empty)

letters = list('Python')               #converting each letter into 'list' items
print(letters)

numbers = list(range(5))                #printing range
print(numbers)



#▪️Nested Lists - Matrix
print("--------------Nested-Lists-Matrix----------------")
mat = [[1,2,3,4],
          [5,6,7,8]]
print(mat)

mixed_mat = [['a', 'b', 'c', 'd'],
             [5,6,7,8]]
print(mixed_mat)
print(type(mixed_mat))



#🔸Access & read - indexing[], Nested Lists(Matrix), slicing(),

#▪️ indexing️[]
print("------------------Indexing[]----------------------")
lsts = ['a','b','c','d']
print(lsts[0], lsts[-1])


#▪️Nested Lists(Matrix)
print("-----------------Nested-Lists-Matrix--------------")
matrix = [
            ['a','b','c','d'],
            ['e','f','g','h'],
            ['i','j','k','l']
]
print(matrix[-1])
print(matrix[-1][-1])
print(matrix[0][2])


#▪️Slicing [start:end]
print("-----------------Slicing-[start:end]----------------")
print(matrix[:])    #printing all
print(matrix[0:2])   #index [[0],[2]]
