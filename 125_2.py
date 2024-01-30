class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

# Test the function
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(""))