n1 = int(input('Enter Lower Limit : '))
n2 = int(input('Enter Upper Limit : '))


# By using Whilw loop
for i in range(n1,n2+1):
    temp = i
    sum = 0
    while temp > 0:
        rem = temp % 10
        temp = temp // 10
        sum = sum + rem ** len(str(i))
    if sum == i:
        print(f'{i} is a Armstrong number')

# By using for loop
# for i in range(n1, n2+1):
#     temp = i
#     sum = 0
#     for j in range(len(str(i))):
#         r = temp % 10
#         temp = temp // 10
#         sum += r ** len(str(i))
#     if sum == i:
#         print(f'{i} is a Armstrong Number')
