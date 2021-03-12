num = int(input('Enter any Number '))
l1 = []
for i in range(num):
    l1.append(i)

result = list(map(lambda a:2**a,l1))
print(result)

for pos,i in enumerate(result):
    print('2 raised to power',pos,'is',i)