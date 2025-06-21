# 01 Booleans

# boolean are generally used in the conditional statements and in flow control

done = True
done = '' # strings are false when they are empty
done = 0 # only zero is considered as false in numbers

if done:
    print('true')
else:
    print('false')    

# list, touple, sets and dict considered as false when they are empty

task_1_done = False
task_2_done = True
task_3_done = False

any_task_done = any([task_1_done,task_2_done,task_3_done]) # give true if any of the value is true

all_task_done = all([task_1_done,task_2_done,task_3_done]) # give true if all the value is true

print(any_task_done)
print(all_task_done)
