power = lambda n: pow(2, n)
n = int(input("Enter a Number : "))
for i in range(n+1):
    print(f'2 Raised to Power {i} is {power(i)}')
