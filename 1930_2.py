class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])

            ans += len(between)

        return ans

# Test Solution
solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))
print(solution.countPalindromicSubsequence("adc"))
print(solution.countPalindromicSubsequence("bbcbaba"))