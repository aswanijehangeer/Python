# Basic Function

def product():
    prod = 12*12
    print(prod)
    
product()

def greet():
    print("Have a great day, Jehangeer")
    
greet()


# Function with argument/parameter

def greeting(name):
    print("Have a good day, " + str(name))
    
greeting('Jehangeer')

# Positional and keyword arguments

def addition(a, b):
    print(a + b)

addition(13, 99)

def subtraction(a, b):
    print(a - b)

subtraction(99, 12)

subtraction(a = 99, b = 12)

# NOTE: position of arguments MATTER.

def result(name = "None", marks = "None"):
    if name != "None" or marks != None:
        print("Name: " + str(name))
        print("Marks: " + str(marks))
        
result()

# Arbitary arguments (*args)

def add(*n):
    sum = 0
    for num in n:
        sum += num
    print(sum)
    
add(34, 34, 4, 66)


# Arbitary Keyword arguments (**kwargs)

def info(**kw):
    for k,v in kw.items():
        print(k, ":", v)

info(name = "Jehangeer", age = 23, marks = 71)


# Returning values

def additions(*n):
    sum = 0
    for num in n:
        sum += num
    return sum

sum = additions(12, 33, 44, 55)
print(sum)

## Pass keyword

def Function():
    pass

# NOTE: don't have any content then don't write function



# Lambda function

sub = lambda n,m : n - m

print(sub(19, 5))




# Removing duplicates from a LIST

listt = [12, 12, 13, 14, 5, 5, 44, 44, 76, 19, 34, 19]

def remove_dup(l):
    unique = set(l)
    u = list(unique)
    u.sort()
    return u

print(listt)
print(remove_dup(listt))



# Redefining built-in type function

def type_dt(data):
    dt = str(type(data))
    if 'str' in dt:
        print("String")
    elif 'int' in dt:
        print("Integar")
    elif 'float' in dt:
        print("Floating Point Number")
    elif 'complex' in dt:
        print("Complex Number")
    
print(type(23))
type_dt(34)

























