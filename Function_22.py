# block of reusable code that perform specific task
# types of function
# user defined
# build in


# print a ffunction that print hrllo world

"""def Hel():
    print("Hello world")
Hel()    
Hel()    
Hel()    
Hel()  """  


# types of Argument
# 1.Default Argument
# 2.keywoed argument(named argement)
# 3.Positional argument
# 4.Arbitrary (variable length arguments)

# parameter
# def sum(n1,n2):
#     sum=n1+n2
#     return sum
# #Positional argument
# print(sum(2,3))


# def sum(n1,n2):
#     sum=n1+n2
#     return sum
# #named argument
# print(sum(n1=2,n2=3))


# def sum(n1,n2=0):
#     sum=n1+n2
#     return sum
# #default argument
# print(sum(2))



# *args
def addAllNum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
outut=addAllNum(1,2,3,4,5)    
# print(outut)

"""
args->arguments are taken as tuple
*kwargs->argument are taken as dictionary
"""
# **kwargs (key-value pair argument we pass) keyworded arguments

# def Studentinfo(**kwargs):
#     for x,y in kwargs.items():
#         print(x ,"is",y)
# Studentinfo(name="tanmay",age=25,city="Noida")        
# Studentinfo(name="Ajay",age=24,city="Delhi")        


# def Add(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum     
# n1=int(input("Entre the value of n :"))
# output=Add(n1)
# # print(Add(n))
# print("the sum of number from 1 to n1 is :",output) 

# n2=int(input("Entre the value of n :"))
# output=Add(n2)
# # print(Add(n2))
# print("the sum of number from 1 to n2 is :",output) 



# Nested function

def outerfun():
    x=1
    def innerfun():
        y=1
        z=x+y
        return z
    return innerfun()
print(outerfun())  
# output=outerfun()
# print(output)     