num = int(input('Enter any number '))
temp = num
sum = 0
while temp > 0:
    rem = temp%10
    sum = sum + rem ** len(str(num))
    temp = temp//10

if sum == num:
    print('armstrong number')
else:
    print('not armstrong number')

