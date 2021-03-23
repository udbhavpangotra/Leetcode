class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        number = [True] * n
        number[0] = number[1] = False
        for i in range(2, n):
            if number[i]:
                for j in range(i*i, n, i):
                    number[j] = False
        return sum(number)
    