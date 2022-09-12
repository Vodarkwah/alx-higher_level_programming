#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        sol = a / b
    except ZeroDivisionError:
        sol = None
    finally:
        print('Inside result: {}'.format(sol))

    return sol
