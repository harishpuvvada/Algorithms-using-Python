#Using memoization and recursion

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n,{})        
        
    def helper(self,n,mem):
        if n<=0:return 0
        if n==1:return 1
        if n==2:return 2
            
        if n in mem:
            return mem[n]
        else:
            mem[n] = self.helper(n-1,mem) + self.helper(n-2,mem)
                
        return mem[n]
        
        