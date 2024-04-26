# List example
my_list = [1, 2, 3]
my_list.append(4)       # Mutable - can modify
print(my_list)          # Output: [1, 2, 3, 4]

# Tuple example
my_tuple = (1, 2, 3)
# my_tuple.append(4)    # This will raise an error since tuples are immutable
print(my_tuple)         # Output: (1, 2, 3)


tpl = (1, 2, 4, 4, 6)
Tpl = ("R", "U", "S", "T")

TPL = (*tpl, *Tpl)
print(TPL)

python_tpl = ("Python")
print(python_tpl)


tpl_sorted = tuple(sorted(tpl))
print(tpl_sorted)