class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        digitSum = 0

        while n > 0:
            digit = n % 10
            product *= digit
            digitSum += digit
            n // = 10

        return product - digitSum
