print('Enter Three Numbers')
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
     print(f'{a} is Greater')
elif b>a and b>c:
    print(f'{b} is Greater')
else:
    print(f'{c} is Greater')