class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        totalSum = 0
        DigitSum = 0

        for i in nums :
            totalSum += i

            n = i
            while n > 0 :
                Digit += n % 10
                n //= 10

        return totalSum -  DigitSum
    
