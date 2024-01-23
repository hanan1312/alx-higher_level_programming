#!/usr/bin/python3

def magic_calculation(a, b):
    tmp_res = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('Too far')
                tmp_res += a ** b / i
        except ValueError as val_e:
            result = b + a
            print(val_e)
            break
    else:
        result = tmp_res * a

    return result
