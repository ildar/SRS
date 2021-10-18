#!/usr/bin/env python3

import math


# variant 20
def fn(x):
    if x < 0:
        return -(1.0/2)*x
    elif x < 2:
        return 2-math.sqrt(2*2 - x*x)
    elif x < 4:
        return math.sqrt(2*2 - (x-2)*(x-2))
    else:
        return -(1.0/2)*(x-4)


if __name__ == '__main__':
    x = float(input())
    print(fn(x))
