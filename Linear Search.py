def linear_search(lst, find):
    flag = 0
    for i in lst:
        if find == i:
            flag = 1
            return f'{find} is find at {lst.index(i)+1} location in the List'
            break
    if flag == 0:
        return f'{find} is not in the List'
        
n = int(input('Enter No. of Element in List : '))
lst = []
for i in range(n):
    ele = int(input(f'Enter {i+1} Element of List : '))
    lst.append(ele)
find = int(input('Enter No. you want to search : '))
print(linear_search(lst, find))