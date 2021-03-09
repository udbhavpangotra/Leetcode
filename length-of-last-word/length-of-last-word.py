class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = s.split()
        if len(array) < 1:
            return 0
        else :
            return  len(array[len(array)-1])

        