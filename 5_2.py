class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        def helper(l: int, r: int) -> None:
            nonlocal res, res_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd length
            helper(i, i)
            # even length
            helper(i, i + 1)

        return res

# Test the function
solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
