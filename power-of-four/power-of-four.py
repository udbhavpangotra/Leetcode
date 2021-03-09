class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False
        return (log10(n)/log10(4)) % 1==0
        #     return True
        # else: return False