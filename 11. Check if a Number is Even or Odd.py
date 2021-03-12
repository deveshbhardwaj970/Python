even_odd = lambda a:a%2==0
num = float(input('Enter any number '))
if even_odd(num) == True:
    print(f'{num} is a Even Number')
else:
    print(f'{num} is a Odd Number')