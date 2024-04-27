# Sets - Unordered collection that can only store unique values

sts = {1, 2, 3, 4, 5, 5}
print(sts)

stts = set([1, 2, 4, 5, 5, 6, 7])
# stts[0] # Error
print(stts)

# Sets can not be embeded to a single set

s = {1, 2, 3}
st = {3, 4, 5}
# St = {s, st}
# print(St) # Error (unhasbable type)



# Built-in functions for Sets
st1, st2 = {10, 30, 40}, {50, 30, 100}
st1.add(55)
st1.remove(40)
# st1.remove(12) 
st1.discard(12)
# st1.clear() # Clears everything from st1
# st1.update(st2)
print(st1)


# Mathematical Set Operations

# Union
print(st1 | st2)

# Intersection
print(st1 & st2)

# Difference 
print(st2 - st1)

# Symmetric difference
print(st1 ^ st2)


