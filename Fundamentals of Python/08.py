# User Input 

print('What is your name ?')
name = input()
age = input('How old are you : ')

print(f'Your name is {name}')
print(f'You age is {age} years')

# Control Statements

condition_input = input('Enter (True / False): ').strip()

if condition_input.lower() == 'true':
    print('The condition')
    print('is true')
elif condition_input.lower() == 'false':
    print('The condition')
    print('is false')
else:
    print("You didn't enter a correct value!")
