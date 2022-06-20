#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for f in range(1, 3):
        try:
            if f > a:
                raise Exception('Too far')
            else:
                result += a ** b / f
        except:
            result = b + a
            break
    return result
