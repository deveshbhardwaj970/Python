ll = int(input('Enter lower limit '))
ul = int(input('Enter upper limit '))


for i in range(ll,ul+1):
    if i ==0 or i == 1:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(f'{i}')

print('These are Prime Numbers')

