year = int(input('Enter year you want to check\nthat year is Leap year or Not '))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(f'{year} is a Leap year')
        else:
            print(f'{year} is Not a Leap Year')
    else:
        print(f'{year} is a Leap Year')
else:
    print(f'{year} is Not a Leap Year')