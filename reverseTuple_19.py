# Reversing a tuple
# reversed()->it iterate through a sequence ina reversed order

# n=int(input("Entre no. of character :"))
# list=[]
# for _ in reversed(n):
#     list.append(input("Entre item :"))
# b=tuple(list) 
# print(b) 

#  this code give error because reversed is used in list,tuple,Strings but here n is integer


n=int(input("Entre no. of character :"))
list=[]
for _ in range(n):
    list.append(input("Entre item :"))
print(list)    
b=tuple(reversed(list)) 
print(b) 