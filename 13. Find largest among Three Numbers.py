a = int(input('Enter First Number : '))
b = int(input('Enter Second Number : '))
c = int(input('Enter Third Number : '))
if a > b and a > c :
    print(f'{a} is Greater')
elif b > a and b > c :
    print(f'{b} is Greater')
else:
    print(f'{c} is Greater')