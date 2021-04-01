class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res = ""
        for i in word:
            if i.isalpha() :
                res+=" "
            elif i.isdigit():
                res+=i
                
        res = [int(i) for i in res.split() if i]
        return(len(set(res)))