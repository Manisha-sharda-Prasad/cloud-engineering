# ⭐️ Data Structure:
#Sets {} :- Sets Characteristics, Sets Fundamentals, Sets Math Methods


# 🔸Sets {} Characteristics: (Unordered,️No Duplicates,Not Indexed,Mutable)::::::::::::::::::::::::::
print("----------Unordered/️NoDuplicate/NotIndexed/Mutable---------")
#▪️Unordered - Gives but gives right Order (stored in 'Hashtable' for 'Fast' access 'Hash f()' used):::::::
my_sets = {120, 23, 67, 120}
print("Unordered: ", my_sets)

#▪️No Duplicates - Repetition Only Unique:::::::
print("️No Duplicates: ", my_sets)

#▪️Not Indexed - Position No. Access/ not subscriptable- stores item randomly:::::::
#print("Indexed: ", my_sets[1])

#▪️Mutable - Replaces Item with new:::::::
#my_sets[1] = 89     # Does not support item assignment
my_sets.remove(23)
print("Mutable: ", my_sets)


# 🔸Sets {} Fundamentals methods::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# add,update,operators,remove,discard,pop:
print("---------------Set-Fundamental-(methods) ----------------")
x = {120, 23, 67, 120}

x.add(50)
x.update({1,2})
x |= {9,11}

#x.pop()                                                                 # do not use 'pop()'/ removes random item in Sets{}
x.remove(9)
#x.remove(None) / x.remove(100)                                          # throws 'error' if value not present

x.discard(100), x.discard(None)                                          # Does not throw error if value not present

print("add/update/operators/remove/discard: ", x)                        # returns {}

#print(sorted(x))
print("sorted: ", sorted(x))                                             # returns [] as used 'sorted'



# 🔸Sets {} Math Methods::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#union,Operators,intersection
# union (merging 'Unique' values from 'All Sets' into 'New Set')
print("--------------------Set-Math-Methods --------------------")
a = {120, 23, 67, 120, 40}
b = {121, 24, 68, 121, 40}
c = {122, 25, 69, 122, 40}

print("Union:",a.union(b.union(c)))
print("Operators:",a | b | c)
print("[Union] Sorted():",sorted(a.union(b.union(c))))                      #[] 'sorted()' - optional

print("Intersection value:",a.intersection(b.intersection(c)))              #intersecting/appearing/repeating value in each sets

print("Difference:",a.difference(b))                                        #returns in 'a',not in 'b'
print("Difference:",b.difference(c))                                        ##returns in 'b',not in 'c'
