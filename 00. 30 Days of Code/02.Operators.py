# Day 2: Operators

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal, tip, tax):
    total = int((meal * (100 + tip + tax) / 100) + 0.5)
    print(total)





if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
