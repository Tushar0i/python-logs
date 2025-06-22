# Sets

# sets work like tuples but they are not ordered and we can change them also we can say that they are like dict but that don't have keys

# duplicates are ignore in the set so make sure we have only one 

names_set1 = {'tushar','raja','mahi','rina','sid','samay'}
names_set2 = {'tushar','sid','mahi','samay'}

intersection = names_set1 & names_set2 # items that are common to both the sets 
print(intersection)

union = names_set1 | names_set2 # all items from both the sets
print(union)

compliment = names_set1 - names_set2 # all item that belong to set1 which are not in set2
print(compliment)

ispowerset = names_set1 > names_set2  # do set one include every thing from set2
print(ispowerset)

print(list(names_set2)) # create list from sets

print(len(names_set1)) # lenght of the set

print('tushar' in intersection) # is tushar common to both set
