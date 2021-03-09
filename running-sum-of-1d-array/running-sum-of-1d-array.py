class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = 0
        # i=0
        # arr = []
        for i in range(len(nums)):
            nums[i] = nums[i] + prev
            prev = nums[i]
        return nums