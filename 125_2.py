class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_etr = ""

        for c in s:
            if c.isalnum():
                new_etr += c.lower()
        return new_etr == new_etr[::-1]

# Test the function
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(""))