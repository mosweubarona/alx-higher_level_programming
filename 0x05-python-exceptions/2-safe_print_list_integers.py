#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ele = 0
    for index in range(x):
        try:
            print('{:d}'.format(my_list[index]), end='')
            ele += 1
        except IndexError:
            break
        except Exception:
            pass

    print('')
    return ele
