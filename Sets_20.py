# set is udes to store multiple vaue in a variable
# {}

"""
1.unordered
2.unindexed
3.immutable->we can't update existing values but can add and remove
4.Duplicates are not allowed
5.any datatypr
5.Mix of  daifferente data type 
"""


names={"Tanmay","Ajay","jay","Sohil khan","bahiya"}
# print(set)
# print(len(names))
# print(type(names))

# # Accessing item in set
# for i in names:
#     print(i)

# if a item exists in it 
# if "tanmay" in names:
#     print("tanmay is present in set")
# else:
#     print("tanmay is not present in set")

# add items in set
# names.add("Ashu")
# print(names)

# add another sequence in 
# list2=["lungs","Eyes"]
# names.update(list2)
# print(names)

# names.remove("bahiya")
# print(names)

# names.remove("nimi")
# print(names)

# discard function will not give error whwn item is not present in the set but item is in the set it will not emove it
# names.discard("bahiya")
# print(names)

num1={1,2,3,4}
num2={3,4,5,6}
# print(num1,num2)


# num3=num1.union(num2)
# print(num3)

# num1.update(num2)
# print(num1)
# print(num2)

# for duplicate only
# num1.intersection_update(num2)
# print(num1)
# print(num2)

# keep all values except duplicate
# num1.symmetric_difference_update(num2)
# print(num1)


# ek question that isme 3 list diya that aur hame usme se item batane the jo 3no list me ho