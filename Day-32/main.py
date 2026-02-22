s1 = {1,2,4}
s2 = {4,5}

print(s1.union(s2)) 

print(s1.intersection(s2))

print(s1.difference(s2)) # items that are in s1 but not in s2

print(s1.symmetric_difference(s2)) # items that are in either s1 or s2 but not in both

print(s1.issubset(s2)) # checks if s1 is a subset of s2

print(s1.issuperset(s2)) # checks if s1 is a superset of s2

print(s1.isdisjoint(s2)) # checks if s1 and s2 have no items in common

# print(s1.add(2)) # adds an item to the set

r = s1.remove(2)
print(s1) # removes an item from the set, raises an error if the item is not found

s1.discard(3) # removes an item from the set, does not raise an error if the item is not found
print(s1)

item = s1.pop() # removes and returns an arbitrary item from the set, raises an error if the set is empty
print(item)
print(s1)

del s1 # deletes the set
