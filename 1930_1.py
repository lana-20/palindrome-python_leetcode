import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        l = set()
        r = collections.Counter(s)

        for i in range(len(s)):
            r[s[i]] -= 1
            if r[s[i]] == 0:
                r.pop(s[i])

            for j in range(26):
                c = chr(ord('a') + j)
                if c in l and c in r:
                    res.add((s[i], c))
            l.add(s[i])

        return len(res)

# Test Solution
solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))
print(solution.countPalindromicSubsequence("adc"))
print(solution.countPalindromicSubsequence("bbcbaba"))