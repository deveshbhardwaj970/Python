import cmath
def quad_eq(a, b, c):
    d = pow(b, 2)-(4*a*c)
    x1 = (-b + cmath.sqrt(d))/(2*a)
    x2 = (-b - cmath.sqrt(d))/(2*a)
    return f'The Solutions are {x1} and {x2}'

print('Enter the Cofficients of Quadratic Equations')
a = float(input('Enter the value of \'a\' : '))
b = float(input('Enter the value of \'b\' : '))
c = float(input('Enter the value of \'c\' : '))
print(quad_eq(a, b, c))
