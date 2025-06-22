# Dictionaries
# key value pairs

user = {"name": "David" , "age":24 , 'height':163 ,"weight" : 69 ,"gender": 'M', }

user['name'] = "Steve"

print(user['name'],user['age'])

print(user.get('city','US')) # we can set a default value to city if we didn't find it 

print(user.pop('height'))

print(user.popitem()) # return and remove the last item form the dict

print("name" in user)

print(list(user.keys())) # return a list with all keys
print(list(user.values())) # return a list with all values

user['is_student'] = True # adding an item

del user['weight'] # delete the item

print(list(user.items())) # return a list with all items

print(len(user)) # return the length of the dict

user_copy = user.copy()

print(user_copy)