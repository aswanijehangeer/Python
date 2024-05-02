# Iterate over elements

for ele in [1, 2, 3]:
    print(ele)
    
for e in 'Python':
    print(e)

lst = [10, 13, 15, 19, 25]

for num in lst:
    print(num*2)

lst = ["python", "java","rust", 12, "JavaScript"]

for ele in lst:
    # if ele == "JavaScript":
    #     print(ele)
    #     continue
    if ele == 12:
        continue
    print(ele.capitalize())

for num in range(2, 5):
    print(num)
    print("Loop")

for n in [1, 2, 3]:
    for m in [1, 2, 3]:
        for o in [1, 2, 3]:
            print(n, m, o)


lst = [1, 2, 5, 7, 8, 1, 3, 5, 8]
uniques_lst = []

for num in lst:
    if num in uniques_lst:
        continue
    uniques_lst.append(num)
    
uniques_lst.sort()
print(uniques_lst)


  
lst = [1, 2, 5, 7, 8, 1, 3, 5, 8]
uniques_lst = set(lst)
print(uniques_lst)
   
  