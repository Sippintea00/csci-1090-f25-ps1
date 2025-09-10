# Ask the user for the first number, store the value in a variable
firstnum = int(input('Enter an integer between 10 and 100: '))

# Ask the user for the second number, store the value in a variable
secondnum = int(input('Enter an integer less than 4: '))
            
# Repeat back the numbers
print(f'You entered {firstnum} and {secondnum}')

# Perform calculations. Be careful about string formatting for autograders.
sum_ = firstnum + secondnum
print(f'{firstnum} + {secondnum} = {sum_}')
product = firstnum * secondnum
print(f'{firstnum} * {secondnum} = {product}')
exponent = firstnum ** secondnum
print(f'{firstnum} ** {secondnum} = {exponent}')
modules = firstnum % secondnum
print(f'{firstnum} % {secondnum} = {modules}')
               
