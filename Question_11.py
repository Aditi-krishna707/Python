# a=2
# b="5"
# print(a+b) 
# it will give typeerror because string and int can not be concat


# find the Value        QUESTION-> 8//2+4%2    ans=2












# factorial
n=int(input("entre the value of n "))
def fun(n):
    if(n==1):
        return 1
    x=fun(n-1)*n
    return x
    
print(fun(n))
# you can use for loop too


