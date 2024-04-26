lst = [1, 2, 3, 4, "Python", "Rust", "R", "C++"]
print(lst)
print(lst[4])

lst[-1] = "Java"
print(lst)

odd = [1, 3, 5, 7, 7]
evn = [2, 4, 6, 8]

# num = [odd, evn]
num = [*odd, *evn]

num.sort()

# add in the list
num.append(8)

# remove from the list

# num.remove(4)
# num.pop(6)
# del(num[5])

# descending order
num.reverse()

print(num)

print(num.index(6))

print(num.count(7))

# clearing list
num.clear()

num = num + [1] # we are adding one to empty list
print(num)

print(bool(5 not in num))