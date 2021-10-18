#!/usr/bin/env python3

import math


def fn(x):
    if x < -6:
        return -3.0
    elif x < -3:
        return x+3
    elif x < 3:
        return math.sqrt(3*3 - x*x)
    elif x < 8:
        return (3.0/5)*(x-3)
    else:
        return 3.0


if __name__ == '__main__':
    x = float(input())
    print(fn(x))
