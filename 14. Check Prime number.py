n = int(input('Enter a Number : '))
flag = 0
for i in range(2, int((n/2) + 1)) :
    if n % i == 0 :
        flag = 1
        break
if n == 1 or flag == 1 :
    print(f'{n} is not a Prime Number')
else:
    print(f'{n} is a Prime Number')