# input a, b, c
# save variables
# calculate

import cmath

while True:
    try:
        variables = [float(x) for x in input('Enter a, b, and c values seperated by spaces:  ').split()]
        if len(variables) == 3:
            if variables[0] != 0:
                break
            else:
                print('ERROR. Value "a" cannot be 0.')
                continue
        else:
            print('ERROR. Invaid number of inputs.')
            continue
    except ValueError:
        print('ERROR. Invalid input.')
        continue

a, b, c = variables
answer_1 = 'ERROR'
answer_2 = 'ERROR'


def quad_eq(a, b, c):
    print('a:', a, 'b:', b, 'c:', c)
    answer_1 = (-b + cmath.sqrt(b**2 - 4 * a * c)) / (2 * a)
    answer_2 = (-b - cmath.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print('answer:', answer_1, 'or', answer_2)


try:
    quad_eq(a, b, c)
except ValueError:
    print('ERROR. Invalid calculation.')
