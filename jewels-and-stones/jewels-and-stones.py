class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jw = list(jewels)
        st = list(stones)
        counter = 0
        for i in st:
            for j in jw:
                if i==j:
                    counter+=1
                    # print(counter)
        return counter