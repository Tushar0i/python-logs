# Loops

# while loop
condition = True
while condition == True: # When the condiotion become not true the loops stops
    print('The condition is True')
    condition = False

count = 0
while count < 20:
    print(count)
    count+=1
print("After the loop ends")

# for loop

for thing in range(5):
    print(thing)

items = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
for item in items:
    print(item)

for index , item in enumerate(items):
    print(item, index)    

# Break and continue    

bag = [1,2,3,4,5,6,7,8,9]
for item in bag:
    if item == 3:
        continue # skip
    if item == 7:
        break # pause
    print(item)
