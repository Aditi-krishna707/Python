# dictionary stores key value pairs
# {}
"""
1.ordered
2.Changeable
3.No duplicate keys
4.unindexed
5.Any data type[key value]
"""

phone={
    "tanmay":89898989898,
    "Ajay":43454578879,
    "Sohil khan":6789345690
}
# print(phone)
# print(len(phone))
# print(type(phone))

# Accessing dictonary
# print(phone["tanmay"])
# print(phone.get("tanmay"))

# print all keys of dictionary
# print(phone.keys())

# update value in dict
# phone["tanmay"]=9478855
# print(phone["tanmay"])

# add element in the dictionary
# phone["Ashu"]=4658578
# print(phone)

"""/////////////////////////////////////"""


dict1={
    "name":"tanmay",
    "age":25,
    "place":"Noida"
}

dict2={
    "name":"ajay",
    "age":24,
    "place":"Delhi"
}

# dict1.update(dict2)
# print(dict1)

# remove item from key
# dict1.pop("name")
# print(dict1)

# remove last add item
# dict1.popitem()
# print(dict1)

# empty the dictionary
# dict1.clear()
# print(dict1)


# Accessing

# it will print all the keys
# for i in dict1:
    # print(i)

# it will print all values     
# for i in dict1:
#     print(dict1[i])


# for printing all the key and values
# for i in dict1.items():
#     print(i)

# for i,j in dict1.items():
#     print(i,j)    



# Nested Dictonary
dict3={
    "area1":{
        "A":"478",
        "B":36,
        "c":56
    },
   " area2":{
        "A":"45678",
        "B":3456,
        "c":6
    }
}
print(dict3["area1"]["B"])


# question->find the sum of all number(value) in the from the dictionary
total_sum = 0
for area in dict3.values():
    for value in area.values():
        total_sum += int(value)  # convert to int before adding

print(total_sum)  # Output: 49710
# print(sum(dict3.values()))