# ⭐️ Data Structure:
#Sets {} :-

# 🔸Sets () Characteristics: (Unordered,️No Duplicates,Not Indexed,Mutable)::::::::::::::::::::::::::::::::::::::::::::
print("--------------------Unordered/️No Duplicate/NotIndexed/Mutable--------------------")
#▪️Unordered - Gives but gives right Order (stored in 'Hashtable' for 'Fast' access 'Hash f()' used):::::::
my_sets = {120, 23, 67, 120}
print("Stores Unordered: ", my_sets)

#▪️No Duplicates - Repetition Only Unique:::::::
print("️No Duplicates: ", my_sets)

#▪️Not Indexed - Position No. Access/ not subscriptable- stores item randomly:::::::
#print("Indexed: ", my_sets[1])

#▪️Mutable - Replaces Item with new:::::::
#my_sets[1] = 89     # Does not support item assignment
my_sets.remove(23)
print("Mutable: ", my_sets)


