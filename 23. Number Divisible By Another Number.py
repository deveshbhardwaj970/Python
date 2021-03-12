l1 = []
item = int(input('Enter item present in your list '))

for i in range(item):
    ele = int(input())
    l1.append(ele)

print(l1)

print('number divisible by 13 are ',list(filter(lambda a:a%13==0,l1)))
