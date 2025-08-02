# variable are container that i used to store data
# variable are not need to declear paarticular type(int null,boolean)
# python is Dynamically typed


# rule for var nameing

"""
1.var name must start with letter or _
2.can't start with number
3.it can contain alphanumeric(A-z,0-9) and underscore
4.case-sensitive
5.Can not be any python keyword
"""


# Student_Rollno->snakecase
# StudentRollno->lower camel case  


name="Aditi"
print(type(name))

roll=12;
print(type(roll))

percentage=33.33
print(type(percentage))

is_couple=False
print(type(is_couple))

print(name,roll,percentage,is_couple)
roll=90
print(name,roll,percentage,is_couple)

# seeeeee
# Sting aand inteeger are not able to  concat
# print("My name is "+name+" myroll is "+roll)
print("My name is "+name+" myroll is ",roll)


# seperator
print(name,roll,percentage,is_couple,sep="-")