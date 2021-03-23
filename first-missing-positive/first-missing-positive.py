class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums.sort()
        res=1
        for i in nums:
            if i==res:
                res +=1
#                 print(i)
#                 print(res)
        return res
                