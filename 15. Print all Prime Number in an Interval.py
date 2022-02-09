n1 = int(input('Enter Lower Limit : '))
n2 = int(input('Enter Upper Limit : '))
for i in range(n1, n2 + 1 ) :
    flag = 0
    for j in range(2, int(i / 2) + 1) :
        if i % j == 0 :
            flag = 1
            break
    if i == 1 or flag == 1 :
        continue
    else:
        print(f'{i} is a Prime Number')