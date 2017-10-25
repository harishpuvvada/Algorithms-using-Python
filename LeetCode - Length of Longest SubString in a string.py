class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i
        print usedChar

        return maxLength



#this code is for length of longest substring from index 1
#         maxLength = 0
#         usedChar = defaultdict(int)

#         for i in range(len(s)):
#             if usedChar[ord(s[i])-ord('a')]==0:
#                 maxLength +=1
#                 usedChar[ord(s[i])-ord('a')]+=1
#             else:
#                 return maxLength

#-----------------------------
# from collections import defaultdict
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         maxLength = 0
#         start = 0
#         temp =0
#         usedChar = defaultdict(int)
#         while start < len(s):
#             for i in range(len(s))[start:len(s)]:
#                 if usedChar[ord(s[i])-ord('a')]==0:
#                     temp +=1
#                     usedChar[ord(s[i])-ord('a')]+=1
#                 else:
#                     break
#             start +=1
#             if temp > maxLength:
#                 maxLength = temp
#         return maxLength
