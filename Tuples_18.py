""" use to store multiple values or item in a variable 
()
1.ordered
2.Immutable
3.Duplicates value
4.Any datatype
5.Mix of different datatype"""

# create tuple with item1

# colours=("red","green","black","orange")

# when we are making a tuple with single item then we need to add comma , because some time we use round bracket to distinguised between the code 
# so without comma it may not understand to take it as a tuple
# and if we not add a comma in tuple it will shoe string when we print datatype
# name=("tanmay",)
# print(name)
# print(type(name))
# print(len(name))

# Bparts=tuple(("brain"))
# # one bracket defining constructor and another tuple 
# print(type(Bparts))


# Accessing item in tuple

# colours=("red","green","black","orange","white","grey")
# print(colours[1])
# print(colours[-1])
# print(colours[1:4])
# print(colours[-1:-4])


# check item is present in tuple
# if "green" in colours:
    # print("yes greeen is present")


# traversal
# for i in colours:
    # print(i)



# concation in tuple
# item1=("apple","banana")
# item2=("gulab jamun","kaju kathali")
# print(item1+item2)


# unpacking of colors
# colours=("red","green","black","orange","white","grey")
# colour1,colour2,colour3=colours
# print(colour1,)
# print(colour2)
# print(colour3)
# Your unpacking code is giving an error because the tuple colours has 6 elements 
# but you are trying to unpack it into only 3 variables:\



# colours = ("red", "green", "black", "orange", "white", "grey")
# colour1, colour2, colour3, colour4, colour5, colour6 = colours
# print(colour1,colour2,colour3,colour4)

# colours = ("red", "green", "black", "orange", "white", "grey")
# colour1, colour2, *others = colours
# print(colour1)   # red
# print(colour2)   # green
# print(others)    # ['black', 'orange', 'white', 'grey']

# why we use tuple whwn we have list->because it is eeasy to traverse