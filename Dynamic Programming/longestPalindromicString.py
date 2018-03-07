def longestpalindromicSubstring(s):
    s1 = s
    s2 = s[::-1]  # reverse of a string
    #print("reverse is ",s2)
    return longestCommonSubSeq(s1, s2)


import numpy as np

res = ""

def printStr(ss,s1,m,n):
    global res

    if m==0 or n==0:
        return

    if ss[m][n] == b'd':
        printStr(ss,s1,m-1,n-1)
        res += s1[m-1]
    elif ss[m][n] == b'u':
        printStr(ss, s1, m - 1, n)
    else:                            #ss[m][n] == b'l'
        printStr(ss, s1, m, n - 1)


def longestCommonSubSeq(s1, s2):
    m, n = len(s1), len(s2)
    # if(i==0 or j==0): we dont this case cuz we are initializing matrix with all zeroes
    #   return

    c = np.zeros((m + 1, n + 1)) #matrix with m+1 rows and n+1 columns - all 0s initially
    ss = np.chararray((m + 1, n + 1)) #matrix with m+1 rows and n+1 columns - all 0s initially

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s1[i-1] == s2[j-1]):
                c[i][j] = 1 + c[i - 1][j - 1]
                ss[i][j] = "d" #diagonal acc to cormen text book

            elif(c[i][j - 1] >= c[i - 1][j]):
                c[i][j] = c[i][j - 1]
                ss[i][j] = "l" #left
            else:
                c[i][j] = c[i - 1][j]
                ss[i][j] = "u" #up
    printStr(ss,s1,m,n)
    #print(ss)

    return c[m][n]




print("Length of longest palindromic substring is",int(longestpalindromicSubstring("aabaadbd")))
print("Longest palindromic substring is", res)


# Logic:
# I create reverse of given string
# then call longest common sub seq on these two strings(basic dynamic prog problem)
# result is longest palindromic sub string
