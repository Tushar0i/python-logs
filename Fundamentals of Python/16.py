# Classes
 # - A Class is like an object constructor, or a "blueprint" for creating objects.

# Inheritence in classes
class Animal:
    def walk(self):
        print('Walking . . . ')

# these are the concepts of object orieanted programming

class Dog(Animal): # now the dog is inherinted from animals
    def bark(self): # self will always be there 
        # print('woof!')
        return 'woof!'

    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

rob = Dog('rob',4,'black')

print(rob.name)
print(rob.age)
print(rob.color)
print(rob.bark())
