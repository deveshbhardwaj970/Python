num = int(input('Enter any number upto which you print fibonacci series '))
a = 0
b = 1
if num == 1:
    print(a)
elif num == 2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c = a+b
        print(c)
        a= b
        b = c