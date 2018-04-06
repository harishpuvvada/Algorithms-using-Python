'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

def string_Comp(s):

    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s+"1"

    dic = {}

    for char in s:

        if char in dic:
            dic[char] +=1
        else:
            dic[char] = 1

    final = ''

    for key,value in dic.items():
        final +=key+str(value)

    return final


print(string_Comp('AAAABaa'))
