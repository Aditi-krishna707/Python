# Pass by value || pass by reference 

# pass by value(immutable object->stiring,int,float,tuple)
# when we ass a function a copy of the object is created and assigned to e loacal variable  in  function
# any change made to them  inside the function does not affect the original variable outside function

# def fun(x):
#     x=x+1
#     print("value of x inside the function",x)
# x=1
# fun(x)
# print("value of x outside the function",x)    


# pass by reference->mulable object->dictionatry,list
# areference of actual pbject is passed to location
# change idside the function will affect the original function


# def fun(list):
#     list.append(5)
#     print("value of list inside the function :",list)
# list=[1,2,3,4]    
# fun(list)
# print("value of list outside the function :",list)

# //////////+++++++++++++++++++when we use assignment operator inside the function
# //////
# 
# def fun(list):
#     # list.append(5)
#     list=[7,8,9]
#     print("value of list inside the function :",list)
# list=[1,2,3,4]    
# fun(list)
# print("value of list outside the function :",list)









# predict thr output
x=50
def  fun(x):
    x=2
fun(x)   
print(x)
# ans will be 50 because x is integer that is immutable so copy will be created and actual value will not change


def message(msg,time=1):
    print(msg*time)
message("hello")    
message("world",5)
