#!/bin/python3

import sys


n = int(input().strip())
a = []	# list of lists
diagA = 0
diagB = 0
diff = 0
revCounter = n - 1
for a_i in range(n):
	a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
	a.append(a_t)
	diagA += a_t[a_i]
	print("a_t[%d:][0] = %s" % (revCounter, a_t[revCounter:][0]))
	diagB += a_t[revCounter:][0]
	revCounter -= 1
diff = abs(diagA - diagB)
print (diff)

# 9												 A 		 B
#  6    6    7   -10   9   -3    8    9   -1	 6		-1
#  9    7   -10   6    4    1    6    1    1	 7		 1
# -1   -2    4   -6    1   -4   -6    3    9	 4		-6
# -8    7    6   -1   -6   -6    6   -7    2    -1		-6
# -10  -4    9    1   -7    8   -5    3   -5	-7		-7
# -8   -3   -4    2   -3    7   -5    1   -5	 7		 2
# -2   -7   -4    8    3   -1    8    2    3	 8		-4
# -3    4    6   -7   -7   -8   -3    9   -6	 9		 4
# -2    0    5    4    4    4   -3    3    0	 0		-2
#											   -------------
#											     33		-19
