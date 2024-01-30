class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum([len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s)])

# Test Solution
solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))
print(solution.countPalindromicSubsequence("adc"))
print(solution.countPalindromicSubsequence("bbcbaba"))