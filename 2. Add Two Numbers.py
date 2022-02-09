# def sum(a, b):
#     return a+b
# n1 = int(input('Enter First Number : '))
# n2 = int(input('Enter Second Number : '))
# print(sum(n1, n2))


# By using Lambda function
sum = lambda a, b : a+b
n1 = int(input('Enter First Number : '))
n2 = int(input('Enter Second Number : '))
print('The Sum  of Two Numbers is : ',sum(n1, n2))