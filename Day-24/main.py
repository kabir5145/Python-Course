# Tuples in python
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.

tup = (1, 2, 3, 4, 5,"Green")
print(tup)
print(type(tup))

# Accessing elements in a tuple
print(tup[0]) # Accessing the first element
print(tup[3]) # Accessing the fourth element

# Slicing a tuple
print(tup[1:4]) # Accessing elements from index 1 to 3
print(tup[:3]) # Accessing the first three elements
print(tup[3:]) # Accessing elements from index 3 to the end

# Tuples are immutable, so we cannot change their elements
# tup[0] = 10 # This will raise an error
# However, we can concatenate tuples to create a new tuple
new_tup = tup + (6, 7, 8)
print(new_tup)

# We can also use the built-in functions with tuples
# print(len(tup)) # Length of the tuple
# print(max(tup)) # Maximum value in the tuple (only works with numeric values)
# print(min(tup)) # Minimum value in the tuple (only works with numeric values)
# print(tup.count(2)) # Count the number of occurrences of 2 in the tuple
# print(tup.index("Green")) # Get the index of the first occurrence of "Green" in the tuple





