class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        if n<3:
            return max(nums)
        
        dp = [0]*(n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        i=2
        while i<n:
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            i+=1
        return(max(dp))