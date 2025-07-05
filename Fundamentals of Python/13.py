# functions

# function name should be descriptive


# we can also accept multipal paremeter
def hello(name = 'my friend', age = '***'): # name is a parameter
    print(f"Hello {name} you are {age} years old.")

hello('tushar',19) # we pass arguments while calling the function
hello('rahul',32)
hello() 

# parameter are passed by reference


# Immutable objects: If you "change" them inside a function, you're really just binding the parameter name to a new object — original remains unchanged.
# example are = int,float,str,tuple,bool

# Mutable objects: Changes inside the object (like modifying list elements) will reflect outside the function.
# example are = list, dict, set, bytearray


def change(value):
    value['name'] = 'default user'

val = 1 # this is a immutable object 
valu = {'name':'tushar'} # this is a mutable object 
change(valu)

print(valu)



# Return statements
varib1 = 'something' # this is decleare in global scope 

def return_something(object):
    varib2 = 'something' # this is decleared in a local scope can bw accessed under this function

    print(object)
    object += 1
    incobj = object
    return incobj 

print(return_something(val))

# Nested function

def talk(phase):
    def say(word):
        print(word)

    words = phase.split(' ')
    for word in words:
        say(word)

talk('I am in a boat')           


def count():
    count = 10

    def increment():
        nonlocal count # if we didn't declear it as not local we can't access count from inside the function 
        count += 1
        print(count)

    increment()    
count()

# Closures

def counter():
    count = 0 
    def increment():
        nonlocal count 
        count += 1 
        return count
    
    return increment  # it will not always nake the count zero 

increment = counter()

print(increment()) #1
print(increment()) #2
print(increment()) #3
print(increment()) #4

