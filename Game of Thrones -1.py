# Game of thrones - 1 from Hacker Rank
# Note : for a string to be a anagram, number of letters with odd frequency should be <=0
# Execution: A palindrome must by definition have an even number of letters. The only exception is a string of an odd length (‘aba’) that has exactly one odd letter count.

#!/usr/bin/py
if __name__ == '__main__':
    string = raw_input()
    found = True
    # Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
    oddCnt = 0
    letterCnt = [0] * 26

    for letter in string:
        letterCnt[ord(letter)-ord('a')] += 1

    for cnt in letterCnt:
        oddCnt += cnt % 2

    if oddCnt > 1:
        found = False

    if not found:
        print("NO")
    else:
        print("YES")
