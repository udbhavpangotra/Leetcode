class Solution:
    def missingNumber(self, nums) -> int:
        a = [x for x in nums]
        b = [x for x in range(0,len(nums)+1)]
        return sum(b)-sum(a)
        del(a)
        del(b)