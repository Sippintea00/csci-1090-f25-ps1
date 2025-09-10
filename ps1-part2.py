# Write a function that takes two variables and does all the computations asked
def number_fun(a,b):
    print(f'You entered {a} and {b}')
    sum_ = a + b
    print(f'{a} + {b} = {sum_}')
    product = a * b
    print(f'{a} * {b} = {product}')
    exponent = a ** b
    print(f'{a} ** {b} = {exponent}')
    modules = a % b
    print(f'{a} % {b} = {modules}')
               


# Ask the user for the first number, store the value in a variable
firstnum = int(input('Enter an integer between 10 and 100: '))
secondnum = int(input('Enter an integer less than 4: '))

number_fun(firstnum, secondnum)
