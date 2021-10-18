#!/usr/bin/env python3

import math
import No3_piecewise_fn

if __name__ == '__main__':
    # x1,x2,dx = float(input()), float(input()), float(input())
    x1, x2, dx = -4.0, 9.0, 0.5
    print('X', 'Y', sep='\t')
    print('=', '=', sep='\t')
    x = x1
    while x <= x2:
        print(x, No3_piecewise_fn.fn(x), sep='\t')
        x = x + dx
