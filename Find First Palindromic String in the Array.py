from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for string in words:
            left = 0
            right = len(string)-1
            is_palindrome = True

            while left < right:
                if string[left] != string[right]:
                    is_palindrome = False
                    break
                left += 1
                right -= 1

            if is_palindrome:
              return string
            
        return ""
