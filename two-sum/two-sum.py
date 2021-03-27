class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        # j=1
        res = target 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target=res-nums[i]
                if target - nums[j] == 0 :
                    return [i,j]
                