"""
1.Arithematic operator
2.Assignment operator
3.Comparision operator
4.Logical operator(and or and not)
5.Identity operator(is->(retuen true if both variable are the same object),is not)
6.Membership operator(in,not in)
7.Bitwise operator
"""

# 1.Arithematic operator(+,-,/,*,%,**,//)
# **->exponentiation
# //->floor division

# identity operator
# is->(retuen true if both variable are the same object)
# is not
x=5
y=5
print("x is y ", x is y)
print("x is y ", x is not y)

# is checks identity (same memory).
# == checks equality (same values).

# Membership operator 
# it is used to check weather the value exist(or not ) inside  sequence
# String
# list
# tuple
# set
# dictionary(checks only key)

# | Operator | Meaning                                        |
# | -------- | ---------------------------------------------- |
# | `in`     | Returns `True` if the value is present         |
# | `not in` | Returns `True` if the value is **not** present |

# names=["tanmay","Ashu","Ankus"]
# print("if tanmay is present in names " ,"tanmay" in names)
# print("if tanmay is present in names " ,"tanmay" not in names)

# Bitwise operator(sdealing with 0 and 1)
"""
AND(&)
| A | B | A & B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 0     |
| 1 | 0 | 0     |
| 1 | 1 | 1     |



OR(|)
| A | B | A \| B |
| - | - | ------ |
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |



XOR(^)
| A | B | A ^ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |



NOT(!)
left shift(<<)
right shift(>>)
"""



# operator precedence
# BODMAS->bracket open Division .............

"""
()
**
/, //, %
*
+,-
<<,>>
&,|,^
comparision operator
Logical operator(not ,and ,or)
"""

# solve it 3+2**4/2*5-8//2   ans=39


# type()->to find data type of variable