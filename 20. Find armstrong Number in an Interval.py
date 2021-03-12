ll = int(input('Enter lower limit '))
ul = int(input('Enter upper limit '))

for i in range(ll,ul+1):
    temp = i
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum = sum + rem ** len(str(i))
        temp = temp // 10

    if sum == i:
        print(f'{i} is a armstrong number')

