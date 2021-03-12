num = int(input('Enter any number '))
sum = 0
if num < 0:
    print('plz enter positive number')
else:
    for i in range(num+1):
        sum = sum + i
    print(f'The sum is {sum}')

