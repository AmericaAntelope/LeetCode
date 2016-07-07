## revert integer

import os, sys, math

def reverse(x):
	max_int = 2 ** 31 - 1
	min_int = -(2 ** 31)
	sign = 1
	if x < 0:
		sign = -1
		if x < min_int:
			return 0
		x = -1 * x
	rNumb = 0
	while x > 0:
		if rNumb < max_int / 10:
			rNumb = 10 * rNumb + (x % 10)
		else:
			if rNumb == max_int / 10 and (x % 10) <= 7:
				rNumb = 10 * rNumb + (x % 10)
			else:
				return 0
		x /= 10
	return sign * rNumb

inp = 1534236469
print "Input:", inp
print reverse(inp)