class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square(k):
            if k == 0:
                return 0
            return (k % 10) ** 2 + square(k // 10)
        
        k = n
        tried = {n}
        while k != 1:
            k = square(k)
            if k in tried:
                return False
            tried.add(k)
            
        return True