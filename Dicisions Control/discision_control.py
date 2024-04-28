num1 = 1
num2 = 2
num3 = 0

if num1 != num2:
    print("Num1 is not equal to num2")
    num3 = 3
    
print(num3)

tot = 1122
bought_sale = False
dis = 0

if tot >= 1000 and bought_sale:
  dis = 10
  
total = tot - tot*dis/100
print(tot*dis/100)
print(total)

name = "Jehangeer"
age = 19
status = "Minor"

if age >= 65:
    status = "Senior Citizen"
elif age >= 18 and age <= 64:
    status = "adult"

if age >= 18 and age <= 64:
    status = "Adult"

print(status)


total = 1990
discount = 0

if total >= 1000:
    discount = 10
else:
    discount = 2
    
total_purchase = total - total*discount/100
print(total*discount/100)
print(total_purchase)

Str = 'It\'s python'

if "p" in Str:
    Str = "It's Python"
elif "i" in Str:
    Str.capitalize()
    
print(Str)

lst = ['Python', "Rust", "R", "Java"]

if "Python" not in lst:
    lst.append("Python")
elif "Java" not in lst: 
    lst.append("Java")
else:
    lst.append("JavaScript")
    
print(lst)