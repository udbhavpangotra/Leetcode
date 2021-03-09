class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c = 0
        j=[]
        for i in range(len(nums)):
            if target == nums[i]:
                c=c+1        
        if c>=1:
            for i in range(len(nums)):
                if target == nums[i]:
                    j.append(i)
            return([j[0],j[len(j)-1]])
        else:
            return([-1,-1])
        
                