import os, sys, time

def longestPalindrome(s):
	if len(s) < 2:
            return s[0]
        start = 0
        end = 0
        for i in range(len(s)):
            if (i + 1) < len(s) and s[i] == s[i + 1]:
                step = 1
                while (i - step) >= 0 and (i + 1 + step) < len(s) and s[i - step] == s[i + 1 + step]:
                    step += 1
                if (end - start) < (2 * step):
                    end = i + step
                    start = i - step + 1
            if (i - 1) >= 0 and (i + 1) < len(s) and s[i - 1] == s[i + 1]:
                step = 2
                while(i - step) >= 0 and (i + step) < len(s) and s[i - step] == s[i + step]:
                    step += 1
                if (end - start) < (2 * step - 1):
                    end = i + step - 1
                    start = i - step + 1
        
        return s[start:(end + 1)]

if __name__ == '__main__':
	print longestPalindrome("bb")
	print "What the hell"