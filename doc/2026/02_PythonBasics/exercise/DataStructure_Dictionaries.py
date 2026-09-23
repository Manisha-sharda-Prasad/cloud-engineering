# ⭐️ Data Structure:
# Dictionaries {} :- Dictionaries Characteristics, Methods, Comprehensions


# 🔸 Dictionaries {} Characteristics::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Ordered, ️Duplicate ,NotIndexed(Keyed), Mutable

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
# get(), in, keys(), values(), items(), dict.fromkeys()

print("--------------------Dictionaries{}-Methods--------------------------")
user = {
    'id': 10,
    'age':23,
    'city':"Berlin"
}

# Access - 'get()'- returns 'None' if key 'value' missing
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
print("user : ",user)

# Looping with items()
for key, value in user.items():
    print("items() :",key,":",value)

# add, update, pop(), popitem()
user["name"] = "John"                                                   #add
user["id"] = 0                                                          #update

user.update({"id":105, "city": "Irvine" })                              #update()
print("update() :",user)

user = user.pop("salary", "NOT FOUND")                                  #pop() - if not present ("", "show message")
print("pop():", user)

#user.pop()
#user.popitem()


users = {
    'id': None,
    'name': None,
    'age': None,
    'city': None
}

# Creation - 'dict.fromkeys()' builds 'new dict{}' keys get same 'default value'
users = dict.fromkeys(["id", 'name','age','city'])
print("fromkeys():", users)




# 🔸 Dictionaries {} Comprehensions:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# 3 Components: key-value Expression, Loop, Condition (optional)

#keep only string values & Convert them to UpperCase:

info = {'id': 10, 'name':"John", 'age':23, 'city':"Berlin" }

str_info = {
    key.upper() : value.upper()                 #Expression
    for key, value in info.items()              #Loop
    if isinstance(value, str)                   #Filter
}
print(str_info)

