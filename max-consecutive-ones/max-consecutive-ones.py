class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        count = 0
        check = False
        for i in nums:
            if i==1:
                check=True
                count+=1
            elif i==0:
                l.append(count)
                count=0
                check=False
        if check:
            l.append(count)
        return max(l)