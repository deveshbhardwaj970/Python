n1 = int(input('Enter Lower Limit : '))
n2 = int(input('Enter Upper Limit : '))
sum = 0
if n1 > 0 and n2 > 0 :
    for i in range(n1, n2+1):
        sum += i
    print(f'Sum of Natural Numbers b/w {n1} and {n2} is {sum}')
else : 
    print('Please Enter Positive Limits ')