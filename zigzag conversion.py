##zigzag conversion

import os, sys

def conversion(s, numRows):
	if numRows == 1:
		return s
	if len(s) <= numRows:
		return s
	slist = []
	loc = -1
	dir = 1
	for i in range(len(s)):
		if dir > 0 and loc < (numRows - 1):
			loc += 1
			if len(slist) < numRows:
				slist.append(s[i])
			else:
				slist[loc] += s[i]
			if loc == (numRows - 1):
				dir = -1
		elif dir < 0 and loc > 0:
			loc -= 1
			slist[loc] += s[i]
			if loc == 0:
				dir = 1
	return "".join(slist)

print conversion("PAYPALISHIRING", 10)