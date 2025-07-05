# Object 

# Everything is an object in python

age = 19 # age is a int now it have to all the methds used by an int 
print(age.real)
print(age.imag)
print(age.bit_length())
print(id(age)) # location in memory

# if we did 
age = age + 1 # its will create a new age because int are immuatble
print(id(age))

# in other hand 
list = [1,2,3,4]

print(list)
print(id(list))
# this list will have the same memory address as of previous one because lists are mutable
list.append(5)
print(list)
print(id(list))
