n = int(input('Enter any number upto which you print Fibonacci series : '))
a = 0
b = 1
if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c