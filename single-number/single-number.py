class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # print(nums)
        # print(len(nums))
        if len(nums) < 2 :
            return nums[0]
        elif nums[len(nums)-1] != nums[len(nums)-2]:
            return nums[len(nums)-1]    
        else: 
            i=0
            while i in range(len(nums)-1):
                if nums[i]==nums[i+1]:
                    i = i+2
                    print(i)
                else:
                    return nums[i]
                