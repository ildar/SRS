#!/usr/bin/env python3

import math

def interval_no(x):
    if x<-6:
        return 0
    elif x<-3:
        return 1
    elif x<3:
        return 2
    elif x<8:
        return 3
    else:
        return 4

# main
x = float(input())

interval = interval_no(x)
if interval == 0:
    y = -3.0
elif interval == 1:
    y = x+3
elif interval == 2:
    y = math.sqrt(3*3 - x*x)
elif interval == 3:
    y = (3.0/5)*(x-3)
elif interval == 4:
    y = 3

print(y)
