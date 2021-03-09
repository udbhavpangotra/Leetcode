class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0: return False
        m=log10(n)/log10(3)
        if m%1==0:
            return True
        else:
            return False