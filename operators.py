#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    tip_percent = round(meal_cost * (tip_percent / 100), 2)
    tax_percent = round(meal_cost * (tax_percent / 100), 2)
    meal_cost=math.ceil(meal_cost)
    # print(meal_cost,tip_percent,tax_percent)
    total_cost = (meal_cost) + (tip_percent) + (tax_percent)

    # print(total_cost)
    print("The total meal cost is", int(total_cost), "dollars.")


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
