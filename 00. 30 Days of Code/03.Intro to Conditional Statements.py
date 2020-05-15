# Day 3: Intro to Conditional Statements

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N & 1:
        print('Weird')
    else:
        if 2 <= N < 5:
            print('Not Weird')
        elif 6 <= N <= 20:
            print('Weird')
        else:
            print('Not Weird')





if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
