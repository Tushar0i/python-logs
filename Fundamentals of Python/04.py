# 01 String

"tushar"
'tushar0i'

username = "tushar0i"
username += " is my username"
age = str(19)
print(username)
print(
    '''This 
is a 
multi line 
string'''
)

# 02 String methods

# these methods  don't modify the orignal string

name = 'TUSHAR'
print(name.lower())
print(name.isupper()) # True
print(len(name)) # 6
print("SH" in name) # True
print(name)

# some most common string methods

# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check if a string contains characters or digits and is not empty
# isdecimal() to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower() to check if a string is lowercase
# upper() to get an uppercase version of a string
# isupper() to check if a string is uppercase
# title() to get a capitalized version of a string
# startsswith() to check if the string starts with a specific substring
# endswith() to check if the string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific character separator
# strip() to trim the whitespace from a string
# join() to append new letters to a string
# find() to find the position of a substring

# 03 Escaping Characters in a string

# character after \ is ignored 
example = 'Tushar\n"0i"' # \n all new line
anotherex = "Tushar\"\\oi\""
print(example)
print(anotherex)

# 04  String Characters & Slicing

email = "example@email.com"
print(email[0])
print(email[1])
print(email[-1]) # -ve mean from last 

print(email[8:13]) # start from 8 and ends before 13
print(email[:13]) # empty mean all the way to start or end
print(email[8:])