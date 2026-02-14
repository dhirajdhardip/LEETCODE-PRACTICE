class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sumOfn = 0
        sumOfm = 0

        for i in range(1, n + 1):
            if i % m != 0:      
                sumOfn += i
            else:              
                sumOfm += i

        return sumOfn - sumOfm

