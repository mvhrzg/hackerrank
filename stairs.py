#!/bin/python3

import sys


n = int(input().strip())
steps = "#"
for i in range(n+1, -1, -1):
    if i < n:
        print("%*s%s" % (i, (" "*i), steps*(n-i)))