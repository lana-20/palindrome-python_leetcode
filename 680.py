class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_l, skip_r = s[l + 1:r + 1], s[l:r]
                return (skip_l == skip_l[::-1]
                        or skip_r == skip_r[::-1])
            l, r = l + 1, r - 1
        return True

# Test Solution
solution = Solution()
print(solution.validPalindrome("aba"))
print(solution.validPalindrome("abca"))
print(solution.validPalindrome("abc"))