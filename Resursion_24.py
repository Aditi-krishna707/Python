# # Need?


# # factorial
# n=int(input("entre the value of n "))
# def fun(n):
#     if(n==1):
#         return 1
#     x=fun(n-1)*n
#     return x
    
# print(fun(n))


# print natural number till n

# n=int(input("Entre the value of n"))
# def fun(n):
#     if(n==0):
#         return 
#     print(n)
#     fun(n-1)
# fun(n)


# print natural number till 1 to n

# n=int(input("Entre the value of n"))
# def fun(n):
#     if(n==0):
#         return 
#     fun(n-1)
#     print(n)
# fun(n)


# sum of n numbers

# n=int(input("Entre the value of n "))
# def Add(n):
#     sum=0
#     if(n==0):
#         return 0
#     sum=sum+n
#     ans=Add(n-1)
#     return ans
# print(Add(n))

# def rec_sum(n):
#     if n == 0:
#         return 0
#     return n + rec_sum(n - 1)

# n = int(input("Enter the value of n: "))
# print("Sum is:", rec_sum(n))




# make a function which calculate 'a' raise to the power 'b' using recursion

# don't know error 
# a=int(input("Entre the value of a "))
# b=int(input("Entre the value of b "))
# def pow(a,b):
#     if(b==0):
#         return 1
#     output=a*pow(a,b-1)
#     return output
# print(pow(a,b))

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# def power(a, b):
#     if b == 0:
#         return 1
#     return a * power(a, b - 1)

# print(power(a, b))



# find nth fibonacci term

n=int(input("Entre n :"))
def fibonacci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
for i in range(1,n+1):
    print(fibonacci(i))    
# print(fibonacci(n))    
