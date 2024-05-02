# While Loop 
    
# Prompt from Terminal

# num = input(">")
# print(type(num))

i = 0

while i < 4:
    num = int(input("Number_"))
    if num == 0:
        print("Square:0")
        i += 1
        continue
    if num == 1:
        print("Program exited!")
        break
        
    sq = str(num*num)
    print("Square: " + sq)
    i += 1
else:
    print("Done")
    
    
### Do not use the list.clear() method
lst = [ 1, 4, 56, 2, 4 , 12,  6, 89 ,11, 0]

while lst:  
    lst.pop()  

print("Empty list:", lst)