#Finding Kth largest element in an unsorted array

import random
class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ###### iterative solution
        k = len(nums)-k
        l = 0
        r = len(nums)-1

        while 1:
            pos = self.partition(nums,l,r)
            if pos == k:
                return nums[pos]
            elif pos < k:
                l = pos+1
            else:
                r = pos-1

    def partition(self, array, l, r):
        # randomly pick an index to be the pivot and swap it to the right
        p = random.randint(l,r)
        array[p],array[r] = array[r],array[p]
        privot = array[r]
        boundary = l
        for i in range(l,r):
            if array[i] < privot:
                array[boundary],array[i] = array[i],array[boundary]
                boundary+=1
        array[boundary], array[r] = array[r],array[boundary]
        return boundary
