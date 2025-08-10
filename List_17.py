# what is list?
# it allow you to store multiple itemsin a single variable
"""
1.indexed
2.ordered
3.mutable
4.list can be made of different datatpe
5.a single list can contain different datatype
6.Duplicatesallowed
"""

# a=["Aditi","nimi","jyoti","jay",12.12.5,false]
a=["Aditi","nimi","jyoti","jay"]
# print all list
# print(a)

# checktype of list
# print(type(a))

# find the length of list
# print(len(a))

# check if item is in list
# if "nimi" 

# if a item is not present in the list
# if "tanamy" not in a:
#     print("tanmay is not in this list")


# Accessing in list 
"""
1.indexing
2.range of index(inclusive,exclusive)
3.renage of negative index(-1 se start hoga aur piche se)
4Negative indexing"""

# names=["tanmay","ashu","ankur","ankus","mayank","krishna"]
# print(names[0])
# print(names[-6])
# print(names[1:3])
# print(names[-3:-1])


# adding element to the list
"""
append()->adding item to the end of the list
insert()->it add element at the given index
extend()->when we extend 2 list then the the element of second list come after list 
"""

# names=["tanmay","ashu","ankur","ankus","mayank","krishna"]
# names2=["Aditi","Anushka","priyal","Kratika"]
# names.append("Sohil khan")
# print(names)

# names.insert(2,"TST")
# print(names)

# names.extend(names2)
# print(names)


# Remove element from the list    
# remove()->remove specified item
# pop()->it remove item of the give index ot the last elment

names=["tanmay","ashu","ankur","ankus","mayank","krishna"]
# names.remove("tanmay")
# print(names)

# remove the last element
# names.pop()
# print(names)

# remove element which is at the index 1
# names.pop(1)
# print(names)

# changing item in the list
# at the index
# in the range


marks=[00,10,20,30,40,50,60,70]
# marks[1]=100
# print(marks)

# marks[1:4]=[400]
# SEE CAREFULLY
# print(marks)



# Sorting a list
# nums=[2,5,6,3,33,2,5,68,8]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

# nums.reverse()
# print(nums)


# LIST COMPREHENSION->when we want to make new list from items of the existing list
list=[20,8,5,444,99,20,70,23]
newlist=[]
# for i in list:
#     if i>25:
#         newlist.append(i)
# print(newlist)
# 
# OR
# newlist=[list for lists in list if list > 25 in list] 
# print(newlist)       


# lst = [20, 8, 5, 444, 99, 20, 70, 23]  
# newlist = [x for x in lst if x > 25]
# print(newlist)


# collage=["GLA","SRM","IITB","IITD"]
# newlist=collage.copy()
# print(newlist)

# name1=["tanmay","Ajay","Jay","Akash"]
# name2=["Aditi","Anshu","priyal","Akash"]
# combine=name1+name2
# print(combine)


# Nested list
# num1=[1,2,3,99,100,45]
# num1.insert(2,[55,66,77])
# print(num1)
# print(num1[2][1])



# swap the 
# element of the index 
# nums=[10,20,30,40,50]
# temp=nums[0]
# nums[0]=nums[3]
# nums[3]=temp
# print(nums)


# by takinf user input

n=int(input("Entre the number of elemet in list :"))
list=[]
for _ in range(n):
    num=int(input("Entre element :"))
    list.append(num)
print(list)    
idx1=int(input("idx1 :"))    
idx2=int(input("idx2 :"))    
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp
print(list)