# ⭐️ Data Structure:
# Dictionaries:- Dictionaries Characteristics, Methods


# 🔸 Dictionaries {} Characteristics::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Ordered,️Duplicate,NotIndexed,Mutable

print("----------------Dictionaries{}-Characteristics:---------------------")

mylist = {
          'a': 120,
          #'a': 10,
          'b':23,
          'c':67,
          'd':120
 }
#▪️Ordered - Gives right Order:::::::
print("Ordered: ",mylist)

#▪️No Duplicate(Unique) - allows Repetition/Duplicates:::::::
print("️No Duplicate (Unique): ",mylist)

#▪️Not Indexed(Keyed)- only access with 'key' name:::::::
#print("Indexed: ",mylist[1])
print("Not Indexed (Keyed): ",mylist['b'])

#▪️Mutable - replaces 'original{}' Item with 'new':::::::
mylist[1] = 89
print("Mutable: ",mylist[1])

print("New my_list::",mylist)



# 🔸 Dictionaries {} Methods:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# get(), in, keys(), values(), items()

print("--------------------Dictionaries{}-Methods--------------------------")
user = {
    'id': 10,
    'age':23,
    'city':"Berlin"
}

#Access - 'get()'- returns 'None' if key 'value' missing
print(user["city"])
print("get(): ",user.get("NAME"))

# Checks - 'in' operator - check 'key' inside 'dictionary'
print("In: ","city" in user)
print("In" in user)

# View objects - 'keys()' names in 'dictionary'
print("keys(): ",user.keys())

# View objects - 'values()' names in 'dictionary'
print("values(): ",user.values())

# View objects - 'items()' in 'dictionary' - helps in looping, transforming, compare data[]
print("items(): ",user.items())
#same
print(user)

#Looping with items()
for key, value in user.items():
    print("Key:Value :",key,":",value)

# add, update, pop(), popitem()
user["name"] = "John"                                               #add
user["age"] = 55                                                    #update
user.update({"age":55, "city": "Irvine" })                          #update()
print(user)

user = user.pop("salary", "NOT FOUND")                              #pop() - if not present ("", "show message")
print("Removed Item pop():", user)

#user.pop()
#user.popitem()


users = {
    'id': None,
    'name': None,
    'age': None,
    'city': None
}

#Creation - 'fromkeys()' builds 'new dict{}' keys get same 'default value'
users = dict.fromkeys(["id", 'name','age','city'])
print("fromkeys():", users)

