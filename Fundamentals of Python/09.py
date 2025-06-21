# List

things_list = ['string',1,1.2,2+3j,'tushar',[3009,'item 2 ']]

print('Initial list : ',things_list)

print(f'Initial length of the list {len(things_list)}')

print(f'Item at index 3 is {things_list[3]}')
print("Last element of the list ",things_list[-1]) # first -1 refers to the list with in the list and another -1 refer to the item within that list

print(f'Last element of the things_list is a list so the first elemant of it is {things_list[-1][0]}')

print("Is tushar in the list ","tushar" in things_list)

print('Changing first item of the list which is inside our things_list to item 1')

things_list[-1][0] = 'item 1 '
print(things_list)

print('Item at index 2,3and 4 are ',things_list[2:5]) # this will print a part of a list starts at index 2 to before 5 means 2,3 and 4 

things_list.append('added by append') # add the item in the list
things_list.extend(['added by extend',0.99])
things_list += ['added by +=']
things_list += 'single'
things_list.remove('s') # remove the item  from the list

print(things_list.pop()) #e # it return the last itm from the list and removes it

things_list.insert(0,'first item')

things_list[1:1] = ['Item1','Item2','Item3']

print(things_list)
print(f'length of the final list is {len(things_list)}')


# Sorthing list 

number_list = [23,6,3,23,576,2,57,0,4,6,34,-1,23,36,-99,12,-2]
print(number_list)
number_list.sort()
print(number_list)

string_list = ['Tushar','tushar','Hii','Apple','Building','Bill','Denmark','new york city']

print(string_list) # upper case have higher priority normally but we can use key

# we can also sort without modifying orignal list 
print(sorted(string_list,key = str.lower))

string_list.sort(key = str.lower)

print(string_list)
