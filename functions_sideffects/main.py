import math

def area(radius):
    a = math.pi * radius**2
    return a

def area2(radius):
    return math.pi * radius**2

def absolute_zero(x):
    if x < 0:
        return -x
    else:
        return x

def cmp(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area2(radius)
    return result

def circle_area2(xc, yc, xp, yp):
    return area2(distance(xc, yc, xp, yp))

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_divisible2(x, y):
    return x % y == 0

def is_between(x, y, z):
    return x <= y <= z

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial2(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial2(n-1)

def factorial3(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)

    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial3(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result

a = factorial3(10)
print(a)
