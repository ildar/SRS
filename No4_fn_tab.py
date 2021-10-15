#!/usr/bin/env python3

import math
import No3_piecewise_fn

if __name__ == '__main__':
    x1,x2,dx = float(input()), float(input()), float(input())
    print('X', 'Y', sep='\t')
    print('=', '=', sep='\t')
    x = x1
    while x<=x2:
        print(x, No3_piecewise_fn.fn(x), sep='\t')
        x = x + dx
