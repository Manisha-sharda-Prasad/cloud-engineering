# ⭐️ ::::::: Data Structure ::::::::
#Sets {} :- Sets Characteristics, Fundamentals, Math Methods, Relationship Methods


# 🔸Sets {} Characteristics:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Unordered,️No Duplicates,Not Indexed,Mutable

print("-----------------Sets{}-Characteristics------------------")
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



# 🔸Sets {} Fundamentals methods::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# add,update,operators,remove,discard,pop:
print("----------------Set-Fundamental-(methods)-----------------")
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




# 🔸Sets {} Math Methods::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#Union, Operators, Intersection, Difference, Symmetric_difference

print("--------------------Set-Math-Methods --------------------")
a = {120, 23, 67, 120, 40}
b = {121, 24, 68, 121, 40}
c = {122, 25, 69, 122, 40}

# union (merging all 'Unique' items from 'All Sets' into 'New Set'):
print("Union:",a.union(b.union(c)))
print("Operators:",a | b | c)
print("[Union] Sorted():",sorted(a.union(b.union(c))))                    #[] 'sorted()' - optional

#intersection (only shared items, appearing/repeating value in each set):
print("Intersection value:",a.intersection(b.intersection(c)))


#difference (present in one set and not in oter):
print("Difference:",a.difference(b))                                      # returns in 'a',not in 'b'
print("Operators:",a - b)                                                 # same '-' as 'difference'
print("Difference:",b.difference(c))                                      # returns in 'b',not in 'c'
print("Operators:",b - c)

#symmetric_difference (opposite of 'difference' non-shared items):
print("Symmetric_Difference:", a.symmetric_difference(b))                 # what not appeared in other set
print( "Operators:",a ^ b)                                                # same '^' as 'symmetric_difference'



# 🔸Sets {} Relationship Methods:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#issubset, issuperset, isdisjoint
print("---------------Set-Relationship-Methods ----------------")
p = {120, 23, 40, 67}
q = {120, 23, 40,}

#issubset (check same items appearing in sets?)
print("Is Subset: ", p.issubset(q))
print("Is Subset: ", q.issubset(p))

#issuperset (check includes 'All' items of other set?)
print("Is superset: ", p.issuperset(q))
print("Is superset: ", q.issuperset(p))

#isdisjoint
print("Is disjoint: ",p.isdisjoint(q))
print("Is disjoint: ",q.isdisjoint(p))

