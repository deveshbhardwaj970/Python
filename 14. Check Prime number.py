num = int(input('Enter any number '))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f'{num} is not a Prime Numbrer')
            print(f'{num} is divided by {i}')
            break
    else:
        print(f'{num} is a Prime Numbrer')
else:
    print(f'{num} is not a Prime Numbrer')