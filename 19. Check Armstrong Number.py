n = int(input('Enter a Number : '))
temp = n
sum = 0

# By using Whilw loop
# while temp > 0 :
#     r = temp % 10
#     temp = temp // 10 
#     sum += r ** len(str(n)) 

# By using for loop
for i in range(len(str(n))):
    r = temp % 10
    temp = temp // 10
    sum += r ** len(str(n))
    
if sum == n:
    print(f'{n} is a Armstrong Number')
else:
    print(f'{n} is not a Armstrong Number')