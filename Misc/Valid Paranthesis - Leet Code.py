class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) %2 !=0:
            return False

        stack = []
        dict = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if (stack == [] or dict[char] != stack.pop()): #.pop spits out last element
                    return False
            
        return stack == []
