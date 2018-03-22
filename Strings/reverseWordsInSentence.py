'''
Reverse words in a String.
Input: Sky is blue in color
Output: color in blue is Sky
'''

def reverseSentece(s):
    rev =""

    for word in reversed(s.split(" ")):
        rev += word+ " "

    return rev


print(reverseSentece("Sky is blue in color"))
