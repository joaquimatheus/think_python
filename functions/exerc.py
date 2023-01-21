def right_justify(s):
    length = len(s)
    cal = int(70 / length)

    print(s * cal)

def do_it():
    right_justify('monty')

def do_twice(f):
    f()
    f()

def square():
    print('+- - - -+- - - -+')
    print('|       |       |')
    print('|       |       |')
    print('|       |       |')
    print('|       |       |')
    print('+- - - -+- - - -+')
    print('|       |       |')
    print('|       |       |')
    print('|       |       |')
    print('|       |       |')
    print('+- - - -+- - - -+')

square()
