#name={"rosh","rintu","arjun","parv","parv"}   #no duplicates

#print(name)# no oder or printing / no order

#set() #define set


#duplicates not allowed
#elements are unordered
#cannot fetch a object using index position in set object
#mutable:  we can add the elements in the set

# name.add("shebu")
# print(name)             #add name

# name.clear()            # remove all elements from the object
# print(name)

# name.pop()                  #pop any element from the set
# print(name)

# name.discard("rosh")          #remove an element from the set if it is a member of the set
# print(name)

#name={"rosh","rintu","arjun","parv","parv"}
#new_names=["abhi","ahem","varu","suha","parv"]
# name.update(new_names)                                #add elements from any collection to set
# print(name)


# name={"rosh","rintu","arjun","parv","parv"}
# new_names={"abhi","ahem","varu","suha","parv"}            #intersection of sets
# new_set=name.intersection(new_names)
# print(new_set)

# name={"rosh","rintu","arjun","parv","parv"}                   #union of  sets
# new_names={"abhi","ahem","varu","suha","parv"}
# new_set=name.union(new_names)
# print(new_set)

# name={"rosh","rintu","arjun","parv","parv"}                #give elements from the set names which is 
# new_names={"abhi","ahem","varu","suha","parv"}                not in new_names as a new set
# new_set=name.difference(new_names)
# print(new_set)

name={"rosh","rintu","arjun","parv","parv"}                #recombine all elements from 2 set and rmove common elemennt
new_names={"abhi","ahem","varu","suha","parv"}                
new_set=name.symmetric_difference(new_names)
print(new_set)