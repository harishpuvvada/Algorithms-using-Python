def firstNotRepeatingCharacter(s): #this returns first non repeating character
    if len(s)==1:
        return s
    seen = {}
    for char in s:
        if char not in seen:
            seen[char]=1
        else:
            seen[char] +=1
    #print(seen)
    if len(seen)!=0:
        for k,v in seen.items():
            if v==1:
                return k
    return "_"


class Solution:  #this returns index of first non repeating character - from leetcode
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabets='abcdefghijklmnopqrstuvwxyz'
        indices = []
        for char in alphabets:
            if s.count(char) == 1:
                indices.append(s.index(char))
        if len(indices) > 0:
            return min(indices)
        else:
            return -1
