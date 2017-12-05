#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positives = 0.000000
negatives = 0.000000
zeroes = 0.000000
for element in arr:
    print(element)
    if element > 0:
        positives += 1
    elif element < 0:
        negatives += 1
    elif element == 0:
        zeroes += 1
print("%6f" % (positives/n))
print("%6f" % (negatives/n))
print("%6f" % (zeroes/n))