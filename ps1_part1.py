# Ask the user for the first number
firstnum = int(input("Enter an integer between 10 and 100: "))
if not (10 <= firstnum <= 100):
    raise ValueError("The first number must be between 10 and 100.")

# Ask the user for the second number
secondnum = int(input("Enter an integer less than 4: "))
if not (secondnum < 4):
    raise ValueError("The second number must be less than 4.")

# Repeat back the numbers
print(f"You entered {firstnum} and {secondnum}")

# Perform calculations
print(f"{firstnum} + {secondnum} = {firstnum + secondnum}")
print(f"{firstnum} * {secondnum} = {firstnum * secondnum}")
print(f"{firstnum} ** {secondnum} = {firstnum ** secondnum}")
print(f"{firstnum} % {secondnum} = {firstnum % secondnum}")