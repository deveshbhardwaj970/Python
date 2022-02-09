y = int(input('Enter a Year that you want to check whether it is a Leap Year or not : \n'))
if y % 4 == 0 :
    if  y % 100 == 0 :
        if y % 400 == 0 :
            print(f'{y} is a Leap Year')
        else:
           print(f'{y} is not a Leap Year')
    else:
        print(f'{y} is a Leap Year')
else:
    print(f'{y} is not a Leap Year')
