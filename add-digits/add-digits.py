class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        elif num%9==0:
            return 9
        else: 
            return num%9
            