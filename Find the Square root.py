import math
# Square of a Number
sq = lambda a : a**2
n = int(input('Enter a Number that You want to Square : '))
print(f'Square of {n} is {sq(n)}')

# by using pow() function
print(f'Square of {n} is {pow(n, 2)}')

# -----------------------------------------------------------------------------

# Square Root of a number
sqroot = lambda a : a**.5
n = int(input('Enter a Number that You want to Square : '))
print(f'Square Root of {n} is {round(sqroot(n))}')

# by using math.sqrt() method
print(f'Square Root of {n} is {round(math.sqrt(n))}')
