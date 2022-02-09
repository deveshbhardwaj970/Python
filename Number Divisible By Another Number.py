l = []
item = int(input('Enter item present in your list : '))
for i in range(item):
    ele = int(input(f'Enter {i+1} item : '))
    l.append(ele)
filtered = filter(lambda a:a%5==0,l)
print('Number divisible by 5 are ')
for i in filtered:
    print(i)
