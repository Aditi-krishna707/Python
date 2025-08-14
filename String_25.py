"""
can be written in 

1.using single quote
2.using double quote
3.using triple quote


4.Immutable
we can create a new string by manuplating original string

"""

name1="tanmay"
name2='jay'
name3='''Ajay'''
# print(name1)
# print(name2)
# print(name3)
# print(type(name1))
# print(type(name2))
# print(type(name3))


"""Multi line String"""

intro='''Hi I am TST
recently placed in CRMnext'''
# print(intro)


"""Array likr indexing in String"""
text='A fsoiieh !'
# print(text[0])
# it will also count space 
# print(text[1])
# print(text[-1])


"""traversing a String"""
# using for loop

name="Aditi"
# for i in name:
    # print(i)


# using list comprehension 



# length of sting 
# print(len(name))



# # find char/substring  in a string
# # find->find function give the index of first occuraance of any character
# favname="Tanmay"
# print(favname.find('n'))
# # if that character iss not in that string then it will give output as -1
# print(favname.find('d'))


# we can also search sub string using find function ans space too
favname="Tanmay Singh"
# print(favname.find("nmay"))
# it will dive output 1 because this sub string is not in sring
# print(favname.find("ne"))
# print(favname.find(" "))



"""Slicing in string"""
# to get somepart of the string 
# syntex[start(inclusive):end(exclusive)]


# name="radha rani"
# print(name[1:7])
# print(name[:7])
# print(name[1:])
# print(name[-3:])
# print(name[-3:-1])


"""Modifing strings"""

name="SoHIl khan"
# print(name.upper())
# print(name.lower())

friend="priyal"
# it will capitalize the first woed in the given string
# print(friend.capitalize())


# Stripping/removing any traling white space
# place="  New Delhi   "
# print(place.strip())
# # no change in original string
# print(place)



# replace()->replace old string with new string 'count' no.of times
# if count is not give all occurance of old string is replaced and
# when we give count =1 the first occurance will be replace only
# so count is optional
# string.replace(old_string,new_string,count)

# intro="hi I am Aditi from bihar.Aditi name is give by my parents"
# print(intro.replace("Aditi","jyoti"))
# print(intro.replace("Aditi","jyoti",1))




# Split
# split is used to split the string into no of sublist
# string.split(sep,maxsplit)
# maxsplit->how many times we want to split at the seperator(these paarameters are optional)
# by default value is space


# name="Tanmay,Ajay,jay,SohilKhan,Shiv,Govind"
# print(name.split(",",2))
# print(name.split(","))


# concatenation
# str1="Aditi"
# str2="jyoti"
# str3=str1+str2
# print(str3)



# formate()
# used to isert variable values in the string

# studentName="Nimi Maharaj"
# marks=100
# str="Student name is {s} and the marks is {m}".format(s=studentName,m=marks)
# print(str)




# Escape character->special character that are used to represent  some non-printable/reserved character in the string
# like \' , \\,\t,\r,\b
# backslace(\)

# check palindrome

# def check_palindrome(str):
#     clear_str=(str.replace(" ","")).lower()
#     reversed_str=clear_str[::-1]
#     return reversed_str==clear_str
# str=input("Entre string  ")
# print(check_palindrome(str))

