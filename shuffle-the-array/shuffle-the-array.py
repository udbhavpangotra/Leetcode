class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        back = nums[n:]
        front = nums[:n]
        # print(front)
        # print(back)
        res = []
        i=0
        for i in range(n):
            res.append(front[i])
            res.append(back[i])
        return res
        