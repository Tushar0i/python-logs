# Operators

# ' = ' is a assignment operator

# 01 Arithematic operators 
# basic math function

print( 1 + 3 ) #  addition
print( 2 - 7 ) #  substraction
print( 2 * 3 ) #  multiplication
print( 2 / 3 ) #  division
print( 3 ** 2) #  exponention
print( 5 % 3 ) #  modulo/ remainder
print( 6 // 4) #  round off divide

num = 10 # 10
num += 2 # 12
num *= 5 # 60
num /= 6 # 10
print(num)

# 02 Comporison operators

a = 3
b = 7
a == b # is equal to (False)
a != b # not equal to (True)
a > b # is grater then (False)
a <= b # is less then or equal to (True)

# 03 Boolean operators

condition1 = True
condition2 = False

not condition2 # True
condition2 or condition1 # True
condition1 and condition2 # False

# or in detail
# or written in an expression return the value of the first operation operand that is not false value or falsie value otherwise ir return the last operand

print( 0 or 1 ) ## 1
print( False or "hii" ) ## "hii"
# Since 1st value is false the we will return the 2nd value
print( "hii" or "byy" ) ## "hii"
# hii is not a false value so we will print that 
print( [] or False ) ## False 
# [] ->> empty space is considered as a falsie value  so we will peint the next one 
print( False or [] ) ## []
# Since our 1st value is false we will print 2nd value 

# and in detail
# and only evaluate 2nd argument if first one is true otherwase it evaluates 2nd one

print( 0 and 1 ) ## 0
# 1st one is 0 so it return 0 only
print( 1 and 0 ) ## 0
# 1st one is true of so it check the 2nd one which is false(0) it mean it return 0
print( 1 and 1 ) ## 1
print( False and "hey" ) ## False
print( "hi" and "hey" ) ## "hey"
print( [] and False ) ## []
print( False and [] ) ## False


# 04 Bitwise operators

# very rarely used

# & performes binary AND
# | performs binary OR
# ^ perform a binary XOR operation
# ~ perform a binary NOT operation
# >> shift right operation
# << shift left operation

# 05 is and in operators

# is called identity operator if same object 
# in called membership operator is containd in a list or some other 

# 06 Ternary operator

def isAdult(age):
    return True if age > 18 else False

print(isAdult(10))