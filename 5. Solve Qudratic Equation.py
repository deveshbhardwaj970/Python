import cmath

def solve_qudratic(a,b,c):
    d = (b**2)-(4*a*c)
    sol1 = (-b + cmath.sqrt(d)) / (2 * a)
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    return f'the solution are {sol1} and {sol2}'

print('enter the cofficients of quadratic equations')
a = float(input())
b = float(input())
c = float(input())

print(solve_qudratic(a,b,c))
