def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f
n = int(input('Enter a Number : '))
print(fact(n))
