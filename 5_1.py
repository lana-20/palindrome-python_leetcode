class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize the result as an empty string as a default case.
        res = ""
        # Set the longest length initially to 0.
        resLen = 0

        # Go through every single character (or rather every single position in this string), considering it to be the center.
        for i in range(len(s)):
            # First, let's check odd length palindromes.
            # odd length
            # We have a left and right pointer, initialized to i, which is our center position right now.
            l, r = i, i
            # While our left and right pointers are in-bound, as well as while this is a palindrome, so we want to check that left and right are equal to each other. We're starting at the middle and expanding outwards. While this is the case, we know this is a palindrome, wo we can potentially update our result.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # We check if the length of this palindrome (r-l+1) is greater than our current result length, then we update the result.
                if (r - l + 1) > resLen:
                    # Update the result and result length.
                    res = s[l:r + 1]
                    resLen = r - l + 1
                # Expand our pointers outwards. Left pointer will be shifted to the left. Right pointer will be shifted to the right.
                l -= 1
                r += 1

            # Now, let's check the even length palindromes as well.
            # even length
            # There are many ways to handle this. What we do is set the left pointer to i and set the right pointer to i+1.
            l, r = i, i + 1
            # Copy/paste the code from above. Can write a function to do that.
            # While it's a palindrome again, we check it's the longest palindrome we've seen so far. If it is, we update our result.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                # Expand pointers outward.
                l -= 1
                r += 1
        # At the end all we have to do is to return our result.
        return res

# Test the function
solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))

# There are a lot of edge cases that could be frustrating with this problem. For me, putting the if statement, checking if it's the longest palindrome inside of a while loop helped. If you put it outside of the loop, it makes it harder.

# Brute Force: check every single substring in the original string and check if it's a palindrome, and get the longest one. We repeat that process with every character. We have to check if a string is a palindrome, we have to scan through the entire string. So for any given substring, to check if it's a palindrome, it takes linear time compleaxity is O(n). How many substrings do we actually have to check? n2, b/c we're checking every single subdtring containing every single character. So, to check if a string is a palindrome we have to do a linear scan O(n) for every single substring O(n2). So the overall time complexity is O(n3).

# Time: O(n2) - To optimize, we can check if a substing is a palindrome. Start in the middle and start ooutwards. For each character, we consider it a center and keep expanding outwards. We take each character, than is n, and expand it outwards for each character, which is n again. So the overall time complaexity is O(n2).
# There's an edge case. How to check for even length palindromes? Remember to handle it in code.
# Space: O(1) - We don't count the answer as part of the space complexity. Thus, all we use are a few integer variables.


